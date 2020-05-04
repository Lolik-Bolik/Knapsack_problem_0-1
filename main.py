import algorithms as algo
import argparse
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
from tqdm import tqdm
import itertools


def draw_statistic(statistic, filename):
    plt.figure(figsize=(15, 8))
    colors = ['k', 'r', 'g', 'c']
    for object, color in zip(statistic.Method_name.unique(), colors):
        method = statistic[statistic['Method_name'] == object]
        plt.plot(method['File_length'], method['Average_Work_time'], color=color, label=object, linewidth=3)
        plt.scatter(method['File_length'], method['Average_Work_time'], color=color)
        plt.grid(True)
        plt.legend(fontsize=18)
        plt.tick_params(labelsize=16)
        plt.xlabel('Размер файла', fontsize=18)
        plt.ylabel('Среднее время, sec.', fontsize=18)
        plt.title('Среднее время работы', fontsize=20)

    plt.savefig(filename)


def main(args):
    with open(args.path) as f:
        file_content = f.read()
        benchmarks = json.loads(file_content)
    if args.make_csv:
        with open('statistic.csv', 'w') as file:
            columns_names = ['File name', 'Method name', 'Work time', 'Result Profit', 'Optim value',
                             'Result Weight', 'Capacity', 'Answer', 'Match', 'Counter', 'Solve Time', 'Get Float Time']
            writer = csv.DictWriter(file, fieldnames=columns_names)
            writer.writeheader()

            for n in tqdm(range(1, len(benchmarks) + 1)):
                capacity = benchmarks[str(n)]["capacity"][0]
                weights = benchmarks[str(n)]['weights']
                profits = benchmarks[str(n)]['profits']
                algorithms = [(name, f(weights, profits, capacity)) for name, f in algo.__dict__.items() if callable(f)]
                for name, algorithm in algorithms:
                    result = algorithm.solve()
                    if 'optim_value' in benchmarks[str(n)].keys():
                        actual_answer = benchmarks[str(n)]['optim_value']
                    else:
                        actual_answer = sum(itertools.compress(profits, benchmarks[str(n)]['optimal']))
                    match = result.profit == actual_answer
                    writer.writerow(
                        {'File name': f'{n}.txt',
                         'Method name': name,
                         'Work time': result.time,
                         'Result Profit': result.profit,
                         'Optim value': actual_answer,
                         'Result Weight': result.weight,
                         'Capacity': capacity,
                         'Match': match,
                         'Counter': result.counter,
                         'Solve Time': result.solve_time,
                         'Get Float Time': result.get_float_time,
                         'Answer': np.asarray(result.answers)})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str,
                        default='./data/low-dimensional.json',
                        help='path to benchmarks files')
    parser.add_argument('-make_csv', type=bool,
                        default=True)
    args = parser.parse_args()
    main(args)


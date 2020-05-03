import requests
import numpy as np
import json
import glob
from tqdm import tqdm


def get_data(path, with_optimum=True):
    with open(path, 'r') as f:
        file = f.read()
        file = file.split('\n')
        # print(file[0])
        capacity = [int(file[0].split(' ')[1])]
        n = int(file[0].split(' ')[0])
        if with_optimum:
            weights = [int(x.split(' ')[1]) for x in file[1:-2]]
            profits = [int(x.split(' ')[0]) for x in file[1:-2]]
            optimal = [int(x) for x in file[-2].split(' ')]
        else:
            weights = [int(x.split(' ')[1]) for x in file[1:]]
            profits = [int(x.split(' ')[0]) for x in file[1:]]
            optimal = []
        parameters = {'capacity': capacity,
                      'n': n,
                      'weights': weights,
                      'profits': profits,
                      'optimal': optimal}
        return parameters


def get_knapsack(n='01'):

    bas_url = 'https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p'

    c = requests.get(bas_url+n+'_c.txt')
    w = requests.get(bas_url+n+'_w.txt')
    p = requests.get(bas_url+n+'_p.txt')
    s = requests.get(bas_url+n+'_s.txt')

    kdct = {'capacity': c.text,
            'weights':  w.text,
            'profits':  p.text,
            'optimal':  s.text}
    kdct = {k: v.split('\n') for k, v in kdct.items()}
    kdct = {k: [int(x) for x in v if len(x)>0] for k, v in kdct.items()}
    print(n, 'is loaded!')

    return kdct


def main():
    complexities = ['low-dimensional', 'large_scale']
    low_d_dict = {}
    large_scale_dict = {}
    for complexity in complexities:
        print('---------------------\n')
        print(complexity)
        files = glob.glob('../data/' + complexity + '/*')
        for i in range(1, len(files) + 1):
            if complexity == complexities[0]:
                knapsack = get_data(files[i - 1], with_optimum=False)
            else:
                knapsack = get_data(files[i - 1])

            with open('../data/' + complexity + '-optimum/' + files[i-1].split('/')[-1], 'r') as f:
                knapsack['optim_value'] = int(f.read())

            # can be optimized and write in one line
            if complexity == complexities[0]:
                low_d_dict[i] = knapsack
            else:
                large_scale_dict[i] = knapsack

            filename = files[i-1].split('/')[-1]
            print(f'../data/{complexity}-optimum/{filename} was processed!')

    with open(f'../data/{complexities[0]}.json', 'w') as f:
        print(f.write(json.dumps(low_d_dict)))
        print('Low dimensional saved!')
    with open(f'../data/{complexities[1]}.json', 'w') as f:
        print(f.write(json.dumps(large_scale_dict)))
        print('Large scale saved!')

    numbers = np.arange(1, 8)
    benchmarks = {int(k): get_knapsack(n='0' + str(k)) for k in numbers}
    with open('../data/benchmarks.json', 'w') as f:
        f.write(json.dumps(benchmarks))


if __name__ == '__main__':
    main()

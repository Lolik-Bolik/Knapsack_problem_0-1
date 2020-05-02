import requests
import numpy as np
import json


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
    numbers = np.arange(1, 8)
    benchmarks = {int(k): get_knapsack(n='0' + str(k)) for k in numbers}
    with open('../data/benchmarks.json', 'w') as f:
        f.write(json.dumps(benchmarks))


if __name__ == '__main__':
    main()

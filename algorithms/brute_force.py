from algorithms.base import Results
from time import time
import itertools
import numpy as np


class ExhaustiveSearch:

    def __init__(self, weights, profits, capacity):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.length = len(self.profits)

    def solve(self):
        result = Results()
        result.time = time()
        # Create all possible variants of knapsack
        nodes = list(itertools.product([0, 1], repeat=self.length))

        for node in nodes:
            result.counter += 1
            weight = sum(itertools.compress(self.weights, node))
            profit = sum(itertools.compress(self.profits, node))
            if weight <= self.capacity and result.profit < profit:
                result.answers = list(node)
                result.profit = profit
                result.weight = weight
        result.time = np.round(time() - result.time, 4)
        return result




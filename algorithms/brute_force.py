from algorithms import Results
from time import time
import itertools


# A naive implementation of 0-1 Knapsack Problem
class ExhaustiveSearch:

    def __init__(self, weights, profits, capacity):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.length = len(self.profits)

    def solve_knapsack_problem(self):
        result = Results()
        result.time = time()
        # Create all possible variants of knapsack
        nodes = list(itertools.product([0, 1], repeat=self.length))

        for node in nodes:
            weight = sum(itertools.compress(self.weights, node))
            profit = sum(itertools.compress(self.profits, node))
            if weight <= self.capacity and result.profit < profit:
                # Actually, we can exclude some nodes cause we don't have negative weights
                # But we don't do that there as it is the most plain implementation
                result.answers = list(node)
                result.profit = profit
                result.weight = weight
        result.time = time() - result.time
        return result




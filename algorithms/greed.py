from algorithms.base import Results
from time import time


class GreedySearch:

    def __init__(self, weights, profits, capacity):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.length = len(self.profits)

    def solve(self):
        result = Results()
        result.time = time()
        result.answers = [0] * self.length
        # Create all possible variants of knapsack
        heuristic = [(idx, profit / weight) for idx, (profit, weight) in enumerate(zip(self.profits, self.weights))]
        heuristic = sorted(heuristic, key=lambda x: x[1], reverse=True)
        for item in heuristic:
            if result.weight + self.weights[item[0]] <= self.capacity:
                result.answers[item[0]] = 1
                result.weight += self.weights[item[0]]
                result.profit += self.profits[item[0]]

        return result




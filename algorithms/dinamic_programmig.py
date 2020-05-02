from algorithms import Results
from time import time


class DynamicSolver:

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def solve_knapsack_problem(self):
        result = Results()
        result.n_operations = 0
        start_time = time()
        knapsack_values = [[0 for x in range(0, self.capacity + 1)] for y in range(0, len(self.items) + 1)]
        for i in range(1, len(self.items) + 1):
            current_weight = self.items[i - 1][1]
            current_value = self.items[i - 1][0]
            for c in range(0, self.capacity + 1):
                if current_weight > c:
                    knapsack_values[i][c] = knapsack_values[i - 1][c]
                else:
                    knapsack_values[i][c] = max(knapsack_values[i - 1][c],
                                                knapsack_values[i - 1][c - current_weight] + current_value)
        finish_time = time()
        result.time = round(finish_time - start_time, 2)
        return [knapsack_values[-1][-1], self.get_knapsack_result_items(knapsack_values)]

    def get_knapsack_result_items(self, knapsack_values):
        sequence = []
        i = len(knapsack_values) - 1
        c = len(knapsack_values[0]) - 1
        while i > 0:
            if knapsack_values[i][c] == knapsack_values[i - 1][c]:
                i -= 1
            else:
                sequence.append(i - 1)
                c -= self.items[i - 1][1]
                i -= 1
            if c == 0:
                break
        return list(reversed(sequence))



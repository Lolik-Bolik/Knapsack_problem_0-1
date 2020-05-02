from algorithms.base import Results
from time import time
import itertools
import cplex
from cplex.exceptions import CplexError


class BranchBound:

    def __init__(self, weights, profits, capacity):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.length = len(self.profits)

    def solve_knapsack_problem(self):
        result = Results()
        result.time = time()
        x_names = ['x' + (str(i)) for i in range(1, self.length + 1)]
        ub = [1] * self.length
        # try:
        solver = cplex.Cplex()
        solver.objective.set_sense(solver.objective.sense.maximize)
        solver.variables.add(obj=self.profits, ub=ub, names=x_names)
        contstraints = [x_names, self.weights]
        rhs = [self.capacity]
        solver.linear_constraints.add(lin_expr=[[x_names, self.weights]],
                                      senses='L',
                                      rhs=[self.capacity],
                                      names=['c1']
                                      )
        solver.solve()
        print(solver.solution.get_values())
        pass
        # except CplexError:
        #     return





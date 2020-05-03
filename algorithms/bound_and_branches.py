from algorithms.base import Results
from time import time
import itertools
import cplex
from cplex.exceptions import CplexError
import numpy as np
import os
import sys


class BranchBound:

    def __init__(self, weights, profits, capacity):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.length = len(self.profits)
        self.curr_lower_bound = 0
        self.optimal_solution = []
        self.counter = 0
        self.solve_time = 0
        self.get_float_time = 0

    def solve(self):
        sys.setrecursionlimit(10000)
        result = Results()
        result.time = time()
        solver, x_names = self.initialize_solver()
        try:
            timer = time()
            solver.solve()
            self.solve_time += (time() - timer)
        except CplexError:
            return result
        solution = solver.solution.get_values()
        is_float = np.mod(solution, 1)
        if self.check_integer(is_float):
            self.optimal_solution = solution
        else:
            # I've checked this, the length of returned np.array is always 1 so we don't have several float variables
            # after solving and that's why I can take zero-indexed element
            lock_variable = self.get_float_values(is_float)[0]
            self.recursive_solve(solver, lock_variable, 'left')
            self.recursive_solve(solver, lock_variable, 'right')
        result.answers = self.optimal_solution
        result.time = time() - result.time
        result.weight = sum(itertools.compress(self.weights, self.optimal_solution))
        result.profit = sum(itertools.compress(self.profits, self.optimal_solution))
        result.counter = self.counter
        result.solve_time = self.solve_time
        result.get_float_time = self.get_float_time

        return result

    def recursive_solve(self, solver, float_variable, branch):
        self.counter += 1
        rhs = [0] if branch == 'left' else [1]
        solver.linear_constraints.add(lin_expr=[[[int(float_variable)], [1]]],
                                      senses='E',
                                      rhs=rhs,
                                      names=[f'c{float_variable}']
                                      )
        try:
            timer = time()
            solver.solve()
            self.solve_time += (time() - timer)
        except CplexError:
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        solution = solver.solution.get_values()
        if solver.solution.get_status() != 1: # This status claims optimal solution
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        obj_value = solver.solution.get_objective_value()
        is_float = np.mod(solution, 1)
        if self.check_integer(is_float):
            if self.curr_lower_bound < obj_value:
                self.curr_lower_bound = obj_value
                self.optimal_solution = solution
                solver.linear_constraints.delete(f'c{float_variable}')
                return
            else:
                solver.linear_constraints.delete(f'c{float_variable}')
                return
        elif self.curr_lower_bound > obj_value:
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        else:
            timer = time()
            lock_variable = self.get_float_values(is_float)[0]
            self.get_float_time += time() - timer
            self.recursive_solve(solver, lock_variable, 'left')
            self.recursive_solve(solver, lock_variable, 'right')
            solver.linear_constraints.delete(f'c{float_variable}')
            return

    @staticmethod
    def check_integer(is_float):
        return np.all(is_float == 0)

    @staticmethod
    def get_float_values(is_float):

        return np.where(is_float != 0)[0]

    def initialize_solver(self):
        x_names = ['x' + (str(i)) for i in range(1, self.length + 1)]
        ub = [1] * self.length
        # try:
        solver = cplex.Cplex()
        solver.set_results_stream(open(os.devnull, 'w'))
        solver.objective.set_sense(solver.objective.sense.maximize)
        solver.variables.add(obj=self.profits, ub=ub, names=x_names)
        solver.linear_constraints.add(lin_expr=[[x_names, self.weights]],
                                      senses='L',
                                      rhs=[self.capacity],
                                      names=['c']
                                      )
        return solver, x_names




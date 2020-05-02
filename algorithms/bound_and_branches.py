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

    def solve(self):
        result = Results()
        result.time = time()
        solver, x_names = self.initialize_solver()
        #solver.variables.advanced.tighten_upper_bounds(4, 0)
        try:
            solver.solve()
        except CplexError:
            return
        solution = solver.solution.get_values()
        if self.check_integer(solution):
            self.optimal_solution = solution
        else:
            float_variables = self.get_float_values(solution)  # TODO: Implement sorting before taking indexes
            for variable in float_variables:
                self.recursive_solve_left(solver, variable)
                self.recursive_solve_right(solver, variable)
        result.answers = self.optimal_solution
        result.time = time() - result.time
        result.weight = sum(itertools.compress(self.weights, self.optimal_solution))
        result.profit = sum(itertools.compress(self.profits, self.optimal_solution))
        result.counter = self.counter
        return result
        # except CplexError:
        #     return
    # Variable is set to zero
    def recursive_solve_left(self, solver, float_variable):
        self.counter += 1
        # It also could be done with solver.linear_constraints.add but I've chosen this way
        # Probably the other one is more correct but this path works, actually ^_^
        solver.linear_constraints.add(lin_expr=[[[int(float_variable)], [1]]],
                                      senses='E',
                                      rhs=[0],
                                      names=[f'c{float_variable}']
                                      )
        try:
            solver.solve()
        except CplexError:
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        solution = solver.solution.get_values()
        # WTF, у меня тут стоят ограничения на переменную, а солвер на них забивает и выдает отрицательное чиисло
        # Поэтому мы залетаем в цикл и ловим recursion depth
        if solver.solution.get_status() != 1: # This status claims optimal solution
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        obj_value = solver.solution.get_objective_value()
        if self.check_integer(solution):
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
            float_variables = self.get_float_values(solution)
            for variable in float_variables:
                self.recursive_solve_left(solver, variable)
                self.recursive_solve_right(solver, variable)
                solver.linear_constraints.delete(f'c{float_variable}')
                return

    # Variable is set to one
    def recursive_solve_right(self, solver, float_variable):
        self.counter += 1
        # It also could be done with solver.linear_constraints.add but I've chosen this way
        # Probably the other one is more correct but this path works, actually ^_^

        solver.linear_constraints.add(lin_expr=[[[int(float_variable)], [1]]],
                                      senses='E',
                                      rhs=[1],
                                      names=[f'c{float_variable}']
                                      )
        try:
            solver.solve()
        except CplexError:
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        solution = solver.solution.get_values()
        if solver.solution.get_status() != 1: # This status claims optimal solution
            solver.linear_constraints.delete(f'c{float_variable}')
            return
        obj_value = solver.solution.get_objective_value()
        if self.check_integer(solution):
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
            float_variables = self.get_float_values(solution)
            for variable in float_variables:
                self.recursive_solve_left(solver, variable)
                self.recursive_solve_right(solver, variable)
                solver.linear_constraints.delete(f'c{float_variable}')
                return

    @staticmethod
    def check_integer(solution):
        return np.all(np.mod(solution, 1) == 0)

    @staticmethod
    def get_float_values(solution):
        return np.where(np.mod(solution, 1) != 0)[0]

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




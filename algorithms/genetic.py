import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
import random
from algorithms.base import Results
from time import time
import itertools


class GeneticSolver:
    def __init__(self, weights, profits, capacity):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity
        self.population = None
        self.population_size = None
        self.num_generations = 20

    def get_result_weight(self, indexes):
        weight = 0
        for i in range(len(self.profits)):
            if i in indexes:
                weight += self.weights[i]
        return weight

    def get_result_profit(self, indexes):
        profit = 0
        for i in range(len(self.profits)):
            if i in indexes:
                profit += self.profits[i]
        return profit

    def set_initial_population(self):
        chromosomes = pow(2, len(self.profits))
        self.population_size = (chromosomes, len(self.profits))
        self.population = np.random.randint(2, size=self.population_size).astype(int)

    def cal_fitness(self):
        fitness = np.empty(self.population.shape[0])

        for i in range(self.population.shape[0]):
            sum_of_profits = np.sum(self.population[i] * self.profits)
            sum_of_weights = np.sum(self.population[i] * self.weights)
            if sum_of_weights <= self.capacity:
                fitness[i] = sum_of_profits
            else:
                fitness[i] = 0
        return fitness.astype(int)

    def selection(self, fitness, num_parents, selection_type='max'):
        fitness = list(fitness)
        new_generation = np.empty((num_parents, self.population.shape[1]))
        if selection_type == 'max':
            for i in range(num_parents):
                if selection_type == 'max':
                    max_fitness_idx = np.where(fitness == np.max(fitness))
                    new_generation[i, :] = self.population[max_fitness_idx[0][0], :]
                    fitness[max_fitness_idx[0][0]] = -1

        elif selection_type == 'RWS':
            survive_chances = [fit_value / sum(fitness) for fit_value in fitness]
            new_generation = random.choices(self.population,
                                              weights=survive_chances,
                                              k=num_parents)
            new_generation = np.asarray(new_generation)

        return new_generation

    def crossover(self, parents, num_offsprings):
        offsprings = np.empty((num_offsprings, parents.shape[1]))
        # change a half of a chromosome
        crossover_point = int(parents.shape[1] / 2)
        # the rate of freq doing crossover
        crossover_rate = 0.4
        i = 0
        while (parents.shape[0] < num_offsprings):
            x = rd.random()
            if x > crossover_rate:
                continue
            parent1_index = i % parents.shape[0]
            parent2_index = (i + 1) % parents.shape[0]
            offsprings[i, 0:crossover_point] = parents[parent1_index, 0:crossover_point]
            offsprings[i, crossover_point:] = parents[parent2_index, crossover_point:]
            i += 1
        return offsprings

    def mutation(self, offsprings):
        mutants = np.empty((offsprings.shape))
        mutation_rate = 0.2
        for i in range(mutants.shape[0]):
            random_value = rd.random()
            mutants[i, :] = offsprings[i, :]
            if random_value > mutation_rate:
                continue
            int_random_value = randint(0, offsprings.shape[1] - 1)
            if mutants[i, int_random_value] == 0:
                mutants[i, int_random_value] = 1
            else:
                mutants[i, int_random_value] = 0
        return mutants

    def test(self, fit_lst, pconverge, n):
        profits = fit_lst.tolist()
        maximum = max(profits)
        max_n = profits.count(maximum)
        # print(sorted(profits))
        self.converged = max_n / n
        if self.converged > pconverge:
            return True
        else:
            return False

    def solve(self):
        result = Results()
        start_time = time()
        self.set_initial_population()
        parameters, fitness_history = [], []
        num_parents = int(self.population_size[0] / 2)
        num_offsprings = self.population_size[0] - num_parents
        for i in range(self.num_generations):
            print(i)
            fitness = self.cal_fitness()
            max_fitness = np.where(fitness == np.max(fitness))
            running_answer = self.population[max_fitness[0][0], :]
            print(running_answer)
            fitness_history.append(fitness)
            new_generation = self.selection(fitness, num_parents)
            offsprings = self.crossover(new_generation, num_offsprings)
            mutants = self.mutation(offsprings)
            self.population[0:new_generation.shape[0], :] = new_generation
            self.population[new_generation.shape[0]:, :] = mutants
        fitness_last_gen = self.cal_fitness()
        max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
        result_answer = self.population[max_fitness[0][0], :]
        finish_time = time()
        result.time = np.round(finish_time - start_time, 4)
        result.weight = sum(itertools.compress(self.weights, result_answer))
        result.answers = result_answer
        result.profit = sum(itertools.compress(self.profits, result_answer))
        return result



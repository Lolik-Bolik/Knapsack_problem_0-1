import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt


class GeneticSolver:
    def __init__(self, profits, weights, capacity, num_generations):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity
        self.population = None
        self.population_size = None
        self.num_generations = num_generations


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

    def selection(self, fitness, num_parents):
        fitness = list(fitness)
        parents = np.empty((num_parents, self.population.shape[1]))
        for i in range(num_parents):
            max_fitness_idx = np.where(fitness == np.max(fitness))
            parents[i, :] = self.population[max_fitness_idx[0][0], :]
            fitness[max_fitness_idx[0][0]] = -999999
        return parents

    def crossover(self, parents, num_offsprings):
        offsprings = np.empty((num_offsprings, parents.shape[1]))
        crossover_point = int(parents.shape[1] / 2)
        crossover_rate = 0.8
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
        mutation_rate = 0.4
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

    def optimize(self):
        parameters, fitness_history = [], []
        num_parents = int(self.population_size[0] / 2)
        num_offsprings = self.population_size[0] - num_parents
        for i in range(self.num_generations):
            fitness = self.cal_fitness()
            fitness_history.append(fitness)
            parents = self.selection(fitness, num_parents)
            offsprings = self.crossover(parents, num_offsprings)
            mutants = self.mutation(offsprings)
            self.population[0:parents.shape[0], :] = parents
            self.population[parents.shape[0]:, :] = mutants
        fitness_last_gen = self.cal_fitness()
        max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
        parameters.append(self.population[max_fitness[0][0], :])
        return parameters, fitness_history




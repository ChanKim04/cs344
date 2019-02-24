"""
Homework01 part1  TSP problem for CS 344 at Calvin College
@author: Chan kIm
@date: 02/21/2019

    - Describe your state and action representations.
        state: cities
        action: pairs of two cities
"""
import random
import string

from search import Problem, hill_climbing, simulated_annealing, exp_schedule
import itertools
import math
import time


class tsp(Problem):

    def __init__(self, initial, coordinates):
        self.initial = initial
        self.coordinates = coordinates

    def actions(self, state):
        actions = []
        for i in range(len(state) - 1):
            for j in range(len(state) - 1):
                if i != j:
                    actions.append([state[i], state[j]])
        return actions

    def result(self, state, swap):
        new_state = state[:]
        city1, city2 = new_state.index(swap[0]), new_state.index(swap[1])
        new_state[city2], new_state[city1] = new_state[city1], new_state[city2]
        return new_state

    def value(self, state):
        length = 0
        start = state[0]
        for i in range(len(state) - 1):
            if i != len(state):
                # to calculate the distance between two cities.
                x1 = self.coordinates.get(state[i])[0]
                y1 = self.coordinates.get(state[i])[1]
                x2 = self.coordinates.get(state[i + 1])[0]
                y2 = self.coordinates.get(state[i + 1])[1]
                length = length + math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        # to calculate the distance between the first city and the last city.
        x1 = self.coordinates.get(state[-1])[0]
        y1 = self.coordinates.get(state[-1])[1]
        x2 = self.coordinates.get(start)[0]
        y2 = self.coordinates.get(start)[1]
        length = length + math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return -length


if __name__ == '__main__':

    # # Set the cities.
    state = ['a', 'b', 'c', 'd', 'e', 'f']
    #
    # # Initialize the x and y coordinates of each city.
    coordinates = {'a': (0.0, 0.0), 'b': (1.0, 2.0), 'c': (2.0, 0.0), 'd': (0.0, 1.0), 'e': (2.0, 1.0), 'f': (1.0, 0.0)}
    print('Start:    ' + str(state))

    # Initialize the tsp problem
    p = tsp(state, coordinates)
    print('Value:    ' + str(p.value(state)))

    # Solve the problem using hill climbing.
    start1 = time.time()
    hill_solution = hill_climbing(p)
    end1 = time.time()
    print('Hill-climbing:')
    print('\tSolution: ' + str(hill_solution))
    print('\tValue:    ' + str(p.value(hill_solution)))
    print('\tTime:    ' + str(end1 - start1))

    # Solve the problem using simulated annealing.
    start2 = time.time()
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    end2 = time.time()
    print('Simulated annealing:')
    print('\tSolution: ' + str(annealing_solution))
    print('\tValue:    ' + str(p.value(annealing_solution)))
    print('\tTime:    ' + str(end2 - start2))

    n = 20
    random_state = []
    random_coordinates = []
    while n != 0:
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(2))
        if random_string not in random_state:
            random_state.append(random_string)
            n -= 1
    n = 20
    while n != 0:
        random_coordinate = (random.choice(range(20)), random.choice(range(20)))
        if random_coordinate not in random_coordinates:
            random_coordinates.append(random_coordinate)
            n -= 1

    coordinates = {}
    for i in range(len(random_state)):
        coordinates[random_state[i]] = random_coordinates[i]

    state = random_state
    print('Start:    ' + str(state))

    # Initialize the tsp problem
    p2 = tsp(state, coordinates)
    print('Value:    ' + str(p2.value(state)))

    # Solve the problem using hill climbing.
    start1 = time.time()
    hill_solution = hill_climbing(p2)
    end1 = time.time()
    print('Hill-climbing:')
    print('\tSolution: ' + str(hill_solution))
    print('\tValue:    ' + str(p2.value(hill_solution)))
    print('\tTime:    ' + str(end1 - start1))

    # Solve the problem using simulated annealing.
    start2 = time.time()
    annealing_solution = simulated_annealing(
        p2,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    end2 = time.time()
    print('Simulated annealing:')
    print('\tSolution: ' + str(annealing_solution))
    print('\tValue:    ' + str(p2.value(annealing_solution)))
    print('\tTime:    ' + str(end2 - start2))

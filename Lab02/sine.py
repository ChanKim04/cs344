"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
@Modified by Chan Kim (ck45) for CS 344 Lab02 at Calvin College
@Date: 02/11/2019
"""
from functools import reduce

from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time

class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)

    p = SineVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    start_hill = time.time()
    hill_solution = hill_climbing(p)
    end_hill = time.time()
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution))
          )
    print('Total time:\t' + str(end_hill - start_hill) + ' sec')

    # Solve the problem using simulated annealing.
    start_sa = time.time()
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    end_sa = time.time()
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution))
          )
    print('Total time:\t' + str(end_sa - start_sa) + ' sec')

    # Restarts
    hc_high_val = 0
    hc_high_x = 0
    sa_high_val = 0
    sa_high_x = 0
    initial_list = []
    hill_result = []
    sa_result = []

    for i in range(maximum):
        initial_list.append(randrange(0, maximum))

    for i in range(len(initial_list)):
        p = SineVariant(initial_list[i], maximum, delta=1.0)
        hill_solution = hill_climbing(p)
        hill_result.append(p.value(hill_solution))
        if p.value(hill_solution) > hc_high_val:
            hc_high_val = p.value(hill_solution)
            hc_high_x = hill_solution

    for i in range(len(initial_list)):
        p = SineVariant(initial_list[i], maximum, delta=1.0)
        annealing_solution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=1000))
        sa_result.append(p.value(annealing_solution))
        if p.value(annealing_solution) > sa_high_val:
            sa_high_val = p.value(annealing_solution)
            sa_high_x = annealing_solution

    print('\nRestarts')
    print('Hill-climbing solution       x: ' + str(hc_high_x)
          + '\tvalue: ' + str(hc_high_val)
          )
    print('The average values of the runs: ' + str(reduce(lambda x, y: x + y, hill_result) / len(hill_result)))
    print('Simulated annealing solution x: ' + str(sa_high_x)
          + '\tvalue: ' + str(sa_high_val)
          )
    print('The average values of the runs: ' + str(reduce(lambda x, y: x + y, sa_result) / len(sa_result)))
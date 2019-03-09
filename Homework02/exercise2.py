"""
Homework02 exercise2  Bayesian network problem for CS 344 at Calvin College
@author: Chan kIm
@date: 03/08/2019
"""

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.12 -  A multiply connected network with conditional probability tables
exercises = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.10, F: 0.50}),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00})
    ])

print("P(Cloudy)")
print(enumeration_ask('Cloudy', dict(), exercises).show_approx())
print(elimination_ask('Cloudy', dict(), exercises).show_approx())
print("P(Sprinker | cloudy)")
print(enumeration_ask('Sprinkler', dict(Cloudy=T), exercises).show_approx())
print(elimination_ask('Sprinkler', dict(Cloudy=T), exercises).show_approx())
print("P(Cloudy| the sprinkler is running and it’s not raining)")
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), exercises).show_approx())
print(elimination_ask('Cloudy', dict(Sprinkler=T, Rain=F), exercises).show_approx())
print("P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)")
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), exercises).show_approx())
print(elimination_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), exercises).show_approx())
print("P(Cloudy | the grass is not wet)")
print(enumeration_ask('Cloudy', dict(WetGrass=F), exercises).show_approx())
print(elimination_ask('Cloudy', dict(WetGrass=F), exercises).show_approx())

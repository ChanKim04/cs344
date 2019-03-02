'''
CS 344 Lab05 Exercise 5.3 at Calvin College

@author: Chan Kim (ck45)
@version 03/01/2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
raise_ex = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.00, (T, F): 0.70, (F, T): 0.90, (F, F): 0.1})
    ])

print("P(Raise | sunny)")
'''
    P(R | s)
    = alpha * P(R, s)
    = alpha * <P(R | s), P(-R | s)>
    = alpha * <0.01 * 0.7, 0.99 * 0.7>
    = alpha * <0.007, 0.693>
    = <0.01, 0.99>
    Raise and sunny are independent; therefore, 0.7, sunny, doesn't affect the result. 
'''
print(enumeration_ask('Raise', dict(Sunny=T), raise_ex).show_approx())
print(elimination_ask('Raise', dict(Sunny=T), raise_ex).show_approx())

print("P(Raise | happy ∧ sunny)")
'''
    P(R | h ^ s)
    = alpha * P(R, h, s)
    = alpha * P(R) * P(s) * P(h | R, s)
    = alpha * P(s) * <P(R) * P(h | R, s), P(-R) * P(h | -R, s)>
    = alpha * 0.7 * <0.01 * 1.0, 0.99 * 0.7>
    = alpha * 0.7 * <0.01, 0.693>
    = alpha * <0.007, 0.4851>
    = <0.0142, 0.986>
    Because of the relationship between Happy and Sunny affects Raise, it makes sense.
'''
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), raise_ex).show_approx())
print(elimination_ask('Raise', dict(Happy=T, Sunny=T), raise_ex).show_approx())

print("P(Raise | happy)")
'''
    >>> P(Raise | happy)
    False: 0.982, True: 0.0185
    False: 0.982, True: 0.0185
'''
print(enumeration_ask('Raise', dict(Happy=T), raise_ex).show_approx())
print(elimination_ask('Raise', dict(Happy=T), raise_ex).show_approx())

print("P(Raise | happy ∧ ¬sunny)")
'''
    >>> P(Raise | happy ∧ ¬sunny)
    False: 0.917, True: 0.0833
    False: 0.917, True: 0.0833
'''
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), raise_ex).show_approx())
print(elimination_ask('Raise', dict(Happy=T, Sunny=F), raise_ex).show_approx())
'''
If Raise is true, the probability of happiness is high. 
Therefore, even if it is not sunny, the probability of happiness increases.
For that reasons, the results make sense.
'''
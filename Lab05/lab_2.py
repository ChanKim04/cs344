'''
CS 344 Lab05 Exercise 5.2 at Calvin College

@author: Chan Kim (ck45)
@version 03/01/2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])

print("P(Cancer | positive results on both tests)\n => P(Cancer | Test1 ∧ Test2)")
'''
    P(C | t1 ^ t2)
    = alpha * P(C, t1, t2)
    = alpha * <P(C | t1 ^ t2), P(-C | t1 ^ t2)>
    = alpha * <0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2>
    = alpha * <0.0081, 0.0396>
    = <0.170, 0.830>
'''
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print(elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

print("P(Cancer | a positive result on test 1, but a negative result on test 2)\n => P(Cancer | Test1 ∧ ¬Test2)")
'''
    P(C | t1 ^ -t2)
    = alpha * P(C, t1, -t2)
    = alpha * <P(C | t1 ^ -t2), P(-C | t1 ^ -t2)>
    = alpha * <0.01 * 0.9 * 0.1, 0.99 * 0.2 * 0.8>
    = alpha * <0.0009, 0.1584>
    = <0.00565, 0.99435>
'''
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
print(elimination_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
'''
To me the results are acceptable. If both tests are true, the probability of diagnosing cancer increases. 
If one test fails, the probability is lower than when two tests are true. 
Interestingly, when one test fails, the probability of a diagnosis of cancer is lower than the probability of cancer.
'''
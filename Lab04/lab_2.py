"""
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
@Modified by Chan Kim (ck45) for CS 344 Lab04 at Calvin College
@Date: 02/22/2019

a. Modify the domain to include a new random variable Rain,
    which takes on values rain or not rain, and then do the following:

    1. How many entries does your full joint probability distribution contain now?
        16 entries
    2. Do the probabilities sum up to 1.0? Should they? Explain why or why not.
        Yes. I consider the probability of rain at 50% for raining and 50% for non-raining. Since each 50% of
        rain and non-rain are multiply by every previous possibility is multiplied. The total variable size becomes twice,
        but the total value is still 1.0.
    3. Did you think that you can use anything other than T or F values for the values for the random variables?
        Explain why or why not.
        Yes, It depends on the current value of the variables. If boolean is the current value of the variables,
        the random variables should be boolean. However, if an integer is the current value of the variable,
        the random variables should be an integer not boolean. To use integers as values of variables,
        we can describe coordinates and its possibility.
    4. Did the probabilities you chose indicate that the value of Rain is independent of the original values?
        It indicates that the value of Rain is independent of the original values since we merely include one variable.
        We can realize that the result is the same as previous when we see the result of
        enumerate_joint_ask('Cavity', {'Toothache': T}, P) is False: 0.4, True: 0.6.

b. Compute the value of P(Toothache|rain). Again, compute this value on pencil and paper,
    and then verify your answer by adding code to compute the specified value.
    (0.054 + 0.006 + 0.008 + 0.032) / (0.054 + 0.006 + 0.036 + 0.004 + 0.008 + 0.032 + 0.072 + 0.288) = 0.2

    >> enumerate_joint_ask('Toothache', {'Rain': T}, P)
        False: 0.8, True: 0.2
"""

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006; P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032; P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006; P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032; P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())

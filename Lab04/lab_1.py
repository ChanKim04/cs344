'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
@Modified by Chan Kim (ck45) for CS 344 Lab04 at Calvin College
@Date: 02/22/2019
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

'''
Compute the value of P(Cavity|catch)
1. First, compute it by hand.
    (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144) = 0.18 / 0.34 = 0.5294
    
2. Verify your answer (and the AIMA implementation) by adding code to compute the specified value.
    >> enumerate_joint_ask(‘Cavity’, {‘Catch’: T}, P)
    False: 0.471, True: 0.529
'''
PC2 = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC2.show_approx())


# To consider a coin's head as true and a coin's tail as false.
H, T = True, False
P2 = JointProbDist(['Coin2', 'Coin1'])
P2[H, H] = 0.25; P2[T, H] = 0.25
P2[H, T] = 0.25; P2[T, T] = 0.25

PC3 = enumerate_joint_ask('Coin2', {'Coin1': H}, P2)
print(PC3.show_approx())

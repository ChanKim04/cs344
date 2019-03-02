'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
@Modified by Chan Kim (ck45) for CS 344 Lab05 at Calvin College
@Date: 03/01/2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

print("P(Alarm | burglary ∧ ¬earthquake)")
'''
    Based on the Figure 14.2
    B   E   P(A)
    t   f   .094
    Therefore, False: 0.06, True: 0.94
    
    >>> P(Alarm | burglary ∧ ¬earthquake)
    False: 0.06, True: 0.94
    False: 0.06, True: 0.94

'''
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print(elimination_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

print("P(John | burglary ∧ ¬earthquake)")
'''
    P(J | b ^ -e) 
    = alpha * P(J, b, -e) 
    = alpha * SUMa P(J, a, b, -e) 
    = alpha * SUMa P(b) * P(-e) * P(J | a) * P(a | b, e) 
    = alpha * P(b) * P(-e) * SUMa P(J | a) * P(a | b, -e) 
    = alpha * P(b) * P(-e) * <0.9 * 0.94 + 0.05 * 0.06, 
                              0.1 * 0.94 + 0.95 * 0.06> 
    = alpha * 0.001 * 0.998 * <0.849, 0.151> 
    = alpha * <0.0008473, 0.0001506>
     = <0.849, 0.151>    
     
    >>> P(John | burglary ∧ ¬earthquake)
    False: 0.151, True: 0.849
    False: 0.151, True: 0.849
'''
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print(elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

print("P(Burglary | alarm)")
'''
    P(B | a) 
    = alpha * P(B, a) 
    = alpha * SUMe P(B, e, a) 
    = alpha * SUMe P(B) * P(e) * P(a | B, e) 
    = alpha * <0.001 * 0.002 * 0.95 + 0.001 * 0.998 * 0.94, 
               0.999 * 0.002 * 0.29 + 0.999 * 0.998 * 0.001>
    = alpha * <0.00094002, 0.001576422>
    = <0.374, 0.626>
    
    >>> P(Burglary | alarm)
    False: 0.626, True: 0.374
    False: 0.626, True: 0.374
'''
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
print(elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())

print("P(Burglary | john ∧ mary)")
'''
    >>> P(Burglary | john ∧ mary)
    False: 0.716, True: 0.284
    False: 0.716, True: 0.284
    It makes sense. Since P(B | a) is False: 0.626 and True: 0.374, 
    when we consider the probability to call John and Mary, 
    the result should be decreased than P(B | a). 
    It is because calling to John and Mary is not guaranteed. 
'''
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
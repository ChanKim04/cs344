% 1. From LPN!
% Exercise 2.1, questions 1, 2, 8, 9, 14 - Give the necessary instantiations.
%   1. bread  =  bread	% true - since the terms unify as they are the same atom.
%   2. 'Bread'  =  bread	% false - since Bread and bread are not the same atom
%   8. food(X)  =  food(bread)		% X = bread - Prolog makes this unification.
%   9. food(bread,X)  =  food(Y,sausage)	% X = sausage, Y = bread    % unification
%   14. meal(food(bread),X)  =  meal(X,drink(beer))	% false     % these don't unify since foodbread) = X = dring(beer) is invalid.

% Exercise 2.2 - Explain how Prolog does its unification and reasoning. 
%   If you have issues getting the results you’d expect, are there things you can do to game the system?
house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X) :- house_elf(X).
magic(X) :- wizard(X).
magic(X) :- witch(X).

%                               Expect          result
% ?-  magic(house_elf).         false           false
% ?-  wizard(harry).            not exist       false
% ?-  magic(wizard).            false           false
% ?-  magic(’McGonagall’).      true            false
% ?-  magic(Hermione).          false?          Hermione = dobby, true, Hermione = hermione, Hermione = 'McGonagall', Hermione = rita_skeeter

% It searches the knowledge base top to bottom, and carries out the unification.

% magic(Hermione)	-	Hermione = _G34	-	house_elf(_G34) -	_G34 = dobby
%                                       -   wizard(_G34)    -   _G34 = hermione
%                                       -   witch(_G34)     -   _G34 = 'McGonagall'
%                                                           -   _G34 = rita_skeeter

% 2. Does inference in propositional logic use unification? Why or why not?

%   Yes, it does.
%   Two terms unify if they are the same term or if they contain variables that can be uniformly instantiated with terms 
%   such a way that the resulting terms are equal such as same atome, same number,  same variable, or same complex term. 

%   The tutorial states it specifically as follows:
%   1. If term1 and term2 are constants, then term1 and term2 unify if and only if they are the same atom, or the same number.
%   2. If term1 is a variable and term2 is any type of term, then term1 and term2unify, and term1 is instantiated to term2 . 
%      Similarly, if term2 is a variable and term1 is any type of term, then term1 and term2 unify, and term2 is instantiated to term1. 
%      (So if they are both variables, they’re both instantiated to each other, and we say that they share values.)
%   3. If term1 and term2 are complex terms, then they unify if and only if:
%       1. They have the same functor and arity, and
%       2. all their corresponding arguments unify, and
%       3. the variable instantiations are compatible. (For example, it is notpossible to instantiate variable X to mia when unifying 
%          one pair of arguments, and to instantiate X to vincent when unifying anotherpair of arguments .)
%    4. Two terms unify if and only if it follows from the previous three clauses that they unify.

% 3. Does Prolog inferencing use resolution? Why or why not?

%   Yes, it does.
%   Processing of unification shows resolution as follows in the second example of 2.2 Proof Search:

   loves(vincent,mia). 
   loves(marcellus,mia). 
   jealous(A,B):-  loves(A,C),  loves(B,C).

%   New satisfied goals:  loves(_G5,_G6),loves(_G7,_G6)

%   By using resolution, it gives four solutions: 
%   X  =  _G5  =  vincent and Y  =  _G7  =  vincent
%   X  =  _G5  =  vincent and Y  =  _G7  =  marcellus
%   X  =  _G5  =  marcellus and Y  =  _G7  =  vincent
%   X  =  _G5  =  marcellus and Y  =  _G7  =  marcellus

%   ?- jealous(X,Y).
%   X = Y, Y = vincent
%   X = vincent,
%   Y = marcellus
%   X = marcellus,
%   Y = vincent
%   X = Y, Y = marcellus
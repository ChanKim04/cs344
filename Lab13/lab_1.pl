% 1. Do these exercises from LPN!.
%   1) Exercise 3.2
in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).
directlyIn(katraina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

% ?- in(katarina,natasha).
%   true
% ?- in(olga, katarina).
%   false

%   2) Exercise 4.5
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([], []).
listtran([X | Y], [W | Z]) :- tran(X, W), listtran(Y, Z).

% ?- listtran([eins,neun,zwei],X).
%   X = [one, nine, two]
% ?- listtran(X,[one,seven,six,two]).
%   X = [eins, sieben, sechs, zwei]

% 2. Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with 
% variables and instatiation)? If so, demonstrate how it’s done; if not, explain why not. If it 
% doesn’t, can you implement one? Why or why not?

% Gneralized Modus Ponens is complete for KBs containing only Horn clauses.
% Since Prolog is built on top of Horn clauses, Prolog implemets a version of generalized 
% modus ponens.

% We can proof by the following example:
likes(X, cake) :- person(X).
eats(X, Y) :- person(X), likes(X, Y).
person(john).

% ?- eats(john, cake).
%	true

% ?- likes(john, cake).
%	true

% 	likes(john, cake) is true, and it is derived by using GMP with likes(X, cake) :- person(X) 
%	and person(john).
%	We also can find that eats(john, cake) is true by using GMP with eats(X, Y) :- person(X), 
%	likes(X, Y), person(john) and likes(john, cake)
%	Therefore, it can be defined that john eats cake.

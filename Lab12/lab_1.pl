% 1. From LPN!

    % Exercise 1.4
    killer(butch). % Butch is a killer.
    marry(mia, marcellus). % Mia and Marsellus are married.
    dead(zed). % Zed is dead.
    kill(marcellus, X) :- footmassage(X, mia). % Marsellus kills everyone who gives Mia a footmassage.
    love(mia, X) :- gooddancer(X). % Mia loves everyone who is a good dancer.
    eat(jules, X) :- nutritious(X); tasty(X). % Jules eats anything that is nutritious or tasty.

    % Exercise 1.5
    wizard(ron).
    hasWand(harry).
    quidditchPlayer(harry).
    wizard(X) :- hasBroom(X), hasWand(X).
    hasBroom(X) :- quidditchPlayer(X).

    % Results 
    % wizard(ron). - true
    % witch(ron). - procedure 'witch(A)' does not exist
    % wizard(hermione). - false
    % witch(hermione). - procedure 'witch(A)' does not exist
    % wizard(harry). - true
    % wizard(Y). - Y = ron, Y = harry
    % witch(Y). - procedure 'witch(A)' does not exist

% 2. Consider the well-known modus ponens. Does Prolog implement a version of modus ponens in propositional logic form? 
% If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?
% A propositional argument form of modus ponens is “If A, then B. A. Therefore, B.” 
% For example, if there is an argument that “If a class is difficult, then a student is depressed. A class is difficult. Therefore a student is depressed,”
% we can form Prolog as 
%    depressed(student) :- difficult(class). % If a class is difficult, then a student is depressed.
%    difficult(class). %  A class is difficult.
%    depressed(student). % Therefore a student is depressed.

% 3. Prolog supports representations in the form of Horn clauses. 
%    Compare and contrast the representational power they provide with that of propositional logic.

%       A Horn clause is a clause with at most one positive literal. In Prolog, Head, that is the left-hand side of the :-, 
%       represents  this characteristic as it places only one term. 

% 4. Logical implementations generally distinguish the basic operations of TELL and ASK. 
%    Does Prolog support this distinction? If so, how; if not, why not?

%       The TELL operation informs the knowledge representation system that the sentence in question is true; 
%       the ASK operation asks the system whether the sentence in question is true.
%       Based on the definition, knowledge base, facts and rules, is TELL that describes some collection of relationships, 
%       and queries are ASK since it asks questions about the information stored in the knowledge bases. 
%       Therefore, Prolog supports TELL and ASK as knowledge base, facts and rules, and queries. 

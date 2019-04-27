% Create a Prolog program that implements the ridiculous inferences used by Sir Bedevere 
% (Terry Jones) to justify the burning of the witch (Connie Booth) in Monte Python's Holy Grail. 
% Load your rules and demonstrate that the woman is indeed a witch.

witch(X) :- burns(X). % a witch burns.
burns(X) :- wood(X). % burning thing is wood.
wood(X) :- floats(X). % wood floats

% bread, apple, small rocks, cider, gravy, cherry, mud, church?,
% led and duck float. 
floats(bread).
floats(apple).
floats(small_rocks).
floats(cider).
floats(gravy).
floats(cherry).
floats(mud).
floats(church).
floats(led).
floats(duck).

% if a woman's weight is the same as a duck, 
% the woman is made of wood. Therefore, the woman is a witch.
floats(X) :- sameweight(X, Y), floats(Y).
sameweight(woman, duck).

% output
% ?- witch(woman)
%   true
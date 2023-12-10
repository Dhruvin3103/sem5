% Define genders
female(sakura).
female(hinata).
female(himawari).
female(tsunade).
male(naruto).
male(sasuke).
male(shikamaru).
male(shikadai).
male(kakashi).
male(boruto).
% Define parent-child relationships
parent(tsunade,sakura).
parent(naruto,boruto).
parent(sasuke,sarada).
parent(kakashi,naruto).
parent(hinata,himawari).
parent(hinata,boruto).
% Define additional parent-child relationships for more complexity
parent(shikamaru,shikadai).
parent(sakura,sarada).
parent(naruto,himawari).

% Define rules for determining mother and father
mother(X,Y):- parent(X,Y), female(X).
father(X,Y):- parent(X,Y), male(X).

% Define rule to check if an individual has a child
haschild(X):- parent(X,_).

% Define rules for determining sisters and brothers
sister(X,Y):- parent(Z,X), parent(Z,Y), female(X), X\==Y.
brother(X,Y):- parent(Z,X), parent(Z,Y), male(X), X\==Y.

binatang(sapi).   % Example: sapi is an animal
punyaTaring(sapi).
makanan(X, daging) :- binatang(X), \+ punyaTaring(X).


:- op(900, fy, neg).
taring(X) :- binatang(X), neg(punyaTaring(X)).
makanan(X, daging) :- taring(X).
makanan(X, daging) :- binatang(X), neg(punyaTaring(X)).

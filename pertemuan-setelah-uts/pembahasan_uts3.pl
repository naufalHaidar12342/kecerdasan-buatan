binatang(sapi).
binatang(singa).
punya_taring(singa).

makan(singa,daging).
makan(sapi,rumput).

makan_daging(X):-binatang(X), punya_taring(X).


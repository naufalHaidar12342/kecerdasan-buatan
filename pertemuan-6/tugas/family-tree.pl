% declares males from left-side
male(ib).
male(gy).
male(hs).
male(ag).
male(mn).
male(rz).
male(haidar).
% declare males from right-side
male(kb).
male(kh).
male(ag).
male(ahm).
male(aa).
male(ar).
male(h).

% declare female from left-side
female(ks).
female(jm).
female(f).
female(lm).
female(hn).
% declare females from right-side
female(sut).
female(as).
female(nr).
female(dn).
female(dl).
female(st).
female(sf).

% declare parents
parent_of(mn,haidar).
parent_of(mn,sf).
parent_of(st,haidar).
parent_of(st,sf).
parent_of(gy,mn).
parent_of(gy,hs).
parent_of(gy,ag).
parent_of(jm,mn).
parent_of(jm,hs).
parent_of(jm,ag).
parent_of(ib,jm).
parent_of(ib,f).
parent_of(ks,jm).
parent_of(ks,f).
parent_of(kb,as).
parent_of(sut,as).
parent_of(kh,aj).
parent_of(kh,ahm).
parent_of(kh,aa).
parent_of(kh,ar).
parent_of(kh,h).
parent_of(as,aj).
parent_of(as,ahm).
parent_of(as,aa).
parent_of(as,ar).
parent_of(as,h).
parent_of(h,dn).
parent_of(h,dl).
parent_of(nr,dn).
parent_of(nr,dl).
parent_of(hs,rz).
parent_of(hs,hn).
parent_of(lm,rz).
parent_of(lm,hn).
% married_to
married(mn,st).
married(gy,jm).
married(kb,sut).
married(ib,ks).
married(gy,jm).
married(hs,lm).
married(kb,sut).
married(kh,as).
married(h,nr).

% define the rules
father_of(Father, Child):-male(Father),parent_of(Father,Child).
mother_of(Mother,Child):-female(Mother),parent_of(Mother,Child).
grandparent_of(Grandparent, Child):-parent_of(Grandparent, Parent),parent_of(Parent, Child).
sibling_of(Sibling1, Sibling2):-parent_of(Parent, Sibling1),parent_of(Parent, Sibling2),Sibling1\==Sibling2.
brother_of(Brother,Person):-male(Brother),sibling_of(Brother,Person).
sister_of(Sister,Person):-female(Sister),sibling_of(Sister,Person).
uncle_of(Uncle,Person):-brother_of(Uncle,Parent),parent_of(Parent,Person).
aunt_of(Aunt,Person):-sister_of(Aunt,Parent),parent_of(Parent,Person).
cousin_of(Cousin,Person):-parent_of(Parent1, Cousin),parent_of(Parent2, Person),sibling_of(Parent1, Parent2).
brother_in_law_of(BrotherInLaw,Person):-brother_of(BrotherInLaw,Spouse),married_to(Spouse,Person).
sister_in_law_of(SisterInLaw,Person):-sister_of(SisterInLaw,Spouse),married_to(Spouse,Person).
parent_in_law_of(ParentInLaw,Person):-parent_of(ParentInLaw,Spouse),married_to(Spouse,Person).
great_grandparent_of(GreatGrandparent, Child):-parent_of(GreatGrandparent, Grandparent),parent_of(Parent, GreatGrandparent).
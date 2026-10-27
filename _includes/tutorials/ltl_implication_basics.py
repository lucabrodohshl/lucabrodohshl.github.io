import spot

stronger = spot.formula("G (p & q)")   # always p and q
weaker = spot.formula("G p")           # always p

# spot.contains(left, right) is True iff L(right) is a subset of L(left).
# "stronger implies weaker" is therefore spot.contains(weaker, stronger).
print(spot.contains(weaker, stronger))   # True:  G(p & q) implies G p
print(spot.contains(stronger, weaker))   # False: G p does not imply G(p & q)

# Equivalence is implication in both directions.
print(spot.are_equivalent("G !(a & b)", "G (b -> !a)"))   # True

# Satisfiability: a formula is unsatisfiable iff its automaton is empty.
print(spot.translate("G p & F !p").is_empty())   # True: no trace satisfies it

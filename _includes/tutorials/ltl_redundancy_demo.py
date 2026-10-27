"""Detect redundant LTL requirements with Spot -- a simplified illustration.

Educational example for https://lucabrodohshl.github.io/tutorials/ltl-property-redundancy/
It shows the idea of LTL property refinement on a toy suite. It is not the
tool evaluated in Brodo, Scalora and Henkler, FSE 2026 (doi:10.1145/3808127).
"""
import spot

# A small requirement suite for a door-and-lift controller, written by
# several teams over time. Keys are requirement IDs, values are LTL formulas.
SUITE = {
    "R1": "G !(door_open & moving)",          # safety team
    "R2": "G (moving -> !door_open)",         # legacy spec
    "R3": "G (request -> X grant)",           # control team
    "R4": "G (request -> F grant)",           # product requirements
    "R5": "GF request -> GF grant",           # fairness requirement
    "R6": "G (request -> grant) & F (request & !grant)",  # merged by mistake
    "R7": "F grant | G !grant",               # vacuous requirement
    "R8": "G (error -> alarm)",               # diagnostics team
    "R9": "G (alarm -> !moving)",             # safety team
    "R10": "G (error -> !moving)",            # safety team
}

formulas = {rid: spot.formula(text) for rid, text in SUITE.items()}
aps = {rid: {str(ap) for ap in spot.atomic_prop_collect(f)}
       for rid, f in formulas.items()}

# The checker caches the automaton of each formula, which pays off when
# many pairs are compared. Its contains(left, right) has the same argument
# order as spot.contains: True iff L(right) is a subset of L(left).
lcc = spot.language_containment_checker()


def refines(strong, weak):
    """True iff L(strong) is a subset of L(weak), i.e. strong implies weak."""
    return lcc.contains(weak, strong)


# Step 1: filter unsatisfiable and valid formulas (automata emptiness).
candidates = []
for rid, f in formulas.items():
    if spot.translate(f).is_empty():
        print(f"{rid}: UNSATISFIABLE - fix it, never use it to cover others")
    elif spot.translate(spot.formula.Not(f)).is_empty():
        print(f"{rid}: VALID (tautology) - constrains nothing")
    else:
        candidates.append(rid)

# Step 2: pairwise refinement. After step 1, a formula can only refine
# another one if both share at least one atomic proposition.
edges = set()
for a in candidates:
    for b in candidates:
        if a != b and aps[a] & aps[b] and refines(formulas[a], formulas[b]):
            edges.add((a, b))

# Step 3: equivalence = refinement in both directions. Keep one representative.
representative = {}
for rid in candidates:
    representative[rid] = next(
        r for r in candidates
        if r == rid or ((r, rid) in edges and (rid, r) in edges)
    )

# Step 4: a representative is redundant if a non-equivalent one refines it.
reps = sorted(set(representative.values()), key=candidates.index)
retained = [r for r in reps
            if not any((s, r) in edges and (r, s) not in edges for s in reps)]

print("\nRefinement relations (stronger => weaker):")
order = candidates.index
for a, b in sorted(edges, key=lambda e: (order(e[0]), order(e[1]))):
    if (b, a) in edges:
        if order(a) < order(b):
            print(f"  {a} is equivalent to {b}")
    else:
        print(f"  {a} refines {b}")

print("\nRetained after pairwise refinement:", ", ".join(retained))
for rid in candidates:
    if rid not in retained:
        covers = [r for r in retained if (r, rid) in edges]
        print(f"  {rid} is covered by {', '.join(covers)}")

# Optional extra step, beyond pairwise refinement: is a retained property
# implied by the conjunction of the others? (Greedy, so the result depends
# on the order and is not guaranteed to be the smallest possible set.)
for rid in list(retained):
    others = [formulas[r] for r in retained if r != rid]
    if others and refines(spot.formula.And(others), formulas[rid]):
        retained.remove(rid)
        print(f"  {rid} is implied by the conjunction of {', '.join(retained)}")

print("\nProperties to model-check:", ", ".join(retained))
conjunction = spot.formula.And([formulas[r] for r in retained])
assert all(refines(conjunction, formulas[rid]) for rid in candidates)
print("Check: the retained set implies every satisfiable requirement.")

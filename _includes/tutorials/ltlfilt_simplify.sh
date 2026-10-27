# --unique removes exact duplicates only: both equivalent formulas survive
ltlfilt --unique -f 'G(moving -> !door_open)' -f 'G !(door_open & moving)'
# Simplifying a conjunction can absorb an implied conjunct ...
ltlfilt -r3 -f 'G(request -> X grant) & G(request -> F grant)'
# ... but the result is one rewritten formula, not a list of requirements
ltlfilt -r3 -f 'G(error -> alarm) & G(alarm -> !moving) & G(error -> !moving)'

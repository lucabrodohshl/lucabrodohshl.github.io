# Print the formula only if it implies the --imply formula
ltlfilt -f 'G(request -> X grant)' --imply='G(request -> F grant)'
ltlfilt -f 'G(request -> F grant)' --imply='G(request -> X grant)'

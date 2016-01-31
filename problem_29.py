def nbrDistinct(aBound, bBound):
    distincts = set([])
    for a in range(2, aBound+1):
        for b in range(2, bBound+1):
            distincts.add(a**b)

    return len(distincts)
def totalLattice(width, height):
    group = width + height
    choose = width
    if height< width:
        choose = height
    paths = 1
    for i in range(1, choose+1):
        paths *= (group - i + 1)/i
    return int(paths)

print(totalLattice(20,20))

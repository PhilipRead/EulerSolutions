def totalLattice(width, height):
    grid = [[0 for x in range(height+1)] for x in range(width+1)]
    for i in range(width):
        grid[i][height] = 1
    for i in range(height):
        grid[width][i] = 1
    for i in range(width-1, -1, -1):
        for j in range(height-1, -1, -1):
            grid[i][j] = grid[i][j+1] + grid[i+1][j]
    return grid[0][0]

print(totalLattice(20,20))

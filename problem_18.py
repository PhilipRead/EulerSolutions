def parseDataFile():
    numss = []
    dataFile = open('problem_18_data.txt')
    for line in dataFile:
        rawNums = line.split()
        nums = []
        for rawNum in rawNums:
            nums.append(int(rawNum))
        numss.append(nums)
    return numss

def maxTreePath():
    rows = parseDataFile()
    for i in range(len(rows)-2, -1, -1):
        curRow = rows[i]
        nextRow = rows[i+1]
        for j in range(0, len(curRow)):
            leftChild = nextRow[j]
            rightChild = nextRow[j+1]
            if leftChild > rightChild:
                curRow[j] += leftChild
            else:
                curRow[j] += rightChild
    return rows[0][0]

print(maxTreePath())

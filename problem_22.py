def getNames():
    namesFile = open('problem_22_data.txt')
    names = namesFile.read().replace('"', '').split(',')
    names.sort();
    return names

def getSumOfNames():
    names = getNames()
    count = 1
    sum = 0
    for name in names:
        nameSum = 0
        for letter in name:
            nameSum += ord(letter) - 64
        sum += nameSum * count
        count += 1

    return sum
hash = dict()

def getCollSeq(num):
    if num == 1:
        return 1
    if num in hash:
        return hash[num]
    collSeq = 1
    if num % 2 == 0:
        collSeq += getCollSeq(num/2)
    else:
        collSeq += getCollSeq(num*3+1)
    hash[num] = collSeq
    return collSeq

def getMaxCollSeq(limit):
    max = 1
    num = 1
    for i in range(1, limit):
        nextMax = getCollSeq(i)
        if nextMax > max:
            max = nextMax
            num = i
    return num

print(getMaxCollSeq(1000000))

def calcFact(num):
    numStr = str(num)[::-1]
    totalNums = []
    for numChar in numStr:
        totalNums.append(int(numChar))

    for factor in range(num-1, 1, -1):
        tempNums = []
        carry = 0
        for n in totalNums:
            nextSum = factor*n + carry
            carry = nextSum // 10
            tempNums.append(nextSum % 10)
        if carry > 0:
            carryStr = str(carry)[::-1]
            for numChar in carryStr:
                tempNums.append(int(numChar))
        totalNums = tempNums

    return sum(totalNums)

print(calcFact(100))

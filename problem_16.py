def doubleLargeNum(nums):
    sums = []
    carry = 0
    for num in nums:
        rawSum = num*2 + carry
        if rawSum > 9:
            carry = 1
            sums.append(rawSum % 10)
        else:
            carry = 0
            sums.append(rawSum)
    if carry > 0:
        sums.append(carry)
    return sums

def sumTwoPowerDigits(power):
    sums = [2]
    for i in range(power-1):
        sums = doubleLargeNum(sums)
    finalSum = 0
    for num in sums:
        finalSum += num
    return finalSum

print(sumTwoPowerDigits(1000))

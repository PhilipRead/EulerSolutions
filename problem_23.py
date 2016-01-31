def getPrimes(n):
    if n % 2 == 0:
        nums = list(range(n-1, 3, -2))
    else:
        nums = list(range(n-2, 3, -2))
    curPrime = 3
    primes = [2, 3]
    while(curPrime*curPrime < n):
        removes = set(list(range(curPrime*curPrime, n, 2*curPrime)))
        numSet = set(nums)
        numSet.difference_update(removes)
        nums = list(numSet)
        nums.sort()
        nums.reverse()
        curPrime = nums.pop()
        primes.append(curPrime)
    
    return sorted(primes + nums)

def getProperFactorsSum(num, primes):
    sum = 1
    curDividend = num
    for prime in primes:
        if curDividend % prime == 0:
            curDividend = curDividend / prime
            primeMult = prime * prime
            while curDividend % prime == 0:
                curDividend = curDividend / prime
                primeMult *= prime
            sum *= (primeMult - 1)/(prime - 1)
        if curDividend == 1:
            break
    return sum - num

def findAbundantNums(numsToCheck, primes):
    if len(numsToCheck) < 0:
        return []
    abundantNums = set([])
    for num in numsToCheck:
        curSum = getProperFactorsSum(num, primes)
        if curSum == num:
            maxNum = numsToCheck[len(numsToCheck)-1] + 1
            abundantNums.update(range(num+num, maxNum, num))
            if num+1 < maxNum:
                abundantNums.update(findAbundantNums([i for i in range(num+1, maxNum+1) if i not in abundantNums and i not in primes], primes))
            return abundantNums
        elif curSum > num:
            abundantNums.add(num)
    return abundantNums

def getNonAbundantsSum():
    primes = getPrimes(28124)
    abundantNums = list(findAbundantNums([i for i in range(2, 28124) if i not in primes], primes))
    abundantNums.sort()

    abundantPairSums = set([])
    for num1 in abundantNums:
        for num2 in abundantNums:
            pairSum = num1 + num2
            if pairSum < 28124:
                abundantPairSums.add(pairSum)
            else:
                break

    return sum([i for i in range(1, 28124) if i not in abundantPairSums])
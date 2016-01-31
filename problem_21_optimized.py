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


def sumAmicables(upToNbr):
    primes = getPrimes(upToNbr)
    numsToCheck = [num for num in range(2, upToNbr) if num not in primes]

    sum = 0
    for num in numsToCheck:
        divisorsSum = getProperFactorsSum(num, primes)
        if divisorsSum < upToNbr and num != divisorsSum and num == getProperFactorsSum(divisorsSum, primes):
            sum += num + divisorsSum

    return sum / 2
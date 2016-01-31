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

def getNumGenPrimes(coefB, coefC, primes):
    numGenPrimes = 0
    n = 0
    nextAns = coefC

    while nextAns in primes:
        numGenPrimes += 1
        n += 1
        nextAns = n * (n + coefB) + coefC

    return numGenPrimes

def getLongestGenPrimes():
    primes = getPrimes(100000)
    possCoefBs = range(-999, 1000, 2)
    possCoefCs = [coefC for coefC in range(1001) if coefC in primes]
    maxGenPrimes = (0,0,0)

    for coefB in possCoefBs:
        for coefC in possCoefCs:
            curNumGenPrimes = getNumGenPrimes(coefB, coefC, primes)
            if curNumGenPrimes > maxGenPrimes[0]:
                maxGenPrimes = (curNumGenPrimes, coefB, coefC)

    print maxGenPrimes
    return maxGenPrimes[1] * maxGenPrimes[2]
            
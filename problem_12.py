def getPrimes(n):
    nums = list(range(n-1, 3, -2))
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
    
    return primes + nums
            
def getTriangleNum(targetNumFacts):
    primes = getPrimes(200000)
    triNum = 1
    numFacts = 1
    triCount = 2
    while(numFacts <= targetNumFacts):
        numFacts = 1
        triNum += triCount
        quotient = triNum
        for prime in primes:
            if prime > quotient:
                break   
            primeFactCount = 0
            while(True):
                if(quotient % prime != 0):
                    break
                primeFactCount += 1
                quotient /= prime
            numFacts *= primeFactCount + 1
        triCount += 1
    return triNum

print(getTriangleNum(500))

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

def getFacts(num, primes):
    numFacts = 1
    quotient = num
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
    return numFacts
    
def getTriangleNum(targetNumFacts, primeLimit):
    primes = getPrimes(primeLimit)
    factHash = dict()
    count = 1
    n1 = 1
    n2 = 1
    factHash[1] = 1 
    numFacts = 1
    while(numFacts <= targetNumFacts):
        count += 1
        if count % 2 == 0:
            temp = n1+2
            n1 = n2
            n2 = temp
        else:
            temp = n1+1
            n1 = n2
            n2 = temp
        if n1 not in factHash:
            factHash[n1] = getFacts(n1, primes)
        if n2 not in factHash:
            factHash[n2] = getFacts(n2, primes)
        numFacts = factHash[n1] * factHash[n2]
    return n1*n2

print(getTriangleNum(500, 1000))


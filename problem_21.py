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

class ProperDivisors:
    def __init__(self, divisors):
        self.divisors = divisors;
        self.divisorsSum = sum(divisors)

    def __repr__(self):
        return 'Divisors: {0}; Sum: {1}'.format(self.divisors, self.divisorsSum)

def getProperDivisors(num, knownProperDivisors, primes):
    if num in knownProperDivisors:
        return knownProperDivisors[num]
    else:
        divisors = set([])
        preDivisors = set([])
        dividend = num
        for prime in primes:
            if dividend % prime == 0:
                newPreDivisors = set([prime])
                dividend = dividend / prime
                divisors.add(dividend)
                if dividend == prime:
                    for divisor in preDivisors:
                        newPreDivisors.add(divisor * prime)
                else:
                    for divisor in preDivisors:
                        divisors.add(divisor * dividend)
                        newPreDivisors.add(divisor * prime)

                    primeMult = prime

                    while dividend % prime == 0:
                        primeMult *= prime
                        newPreDivisors.add(primeMult)
                        dividend = dividend / prime
                        divisors.add(dividend)
                        for divisor in preDivisors:
                            newPreDivisors.add(divisor * dividend)

                preDivisors.update(newPreDivisors)

                if dividend in primes or dividend == 0:
                    divisors.add(1)
                    divisors.update(preDivisors)
                    break

        properDivisors = ProperDivisors(divisors)
        knownProperDivisors[num] = properDivisors
        return properDivisors

def sumAmicables(upToNbr):
    primes = getPrimes(upToNbr)
    knownProperDivisiors = {}
    numsToCheck = [num for num in range(2, upToNbr) if num not in primes]

    sum = 0
    for num in numsToCheck:
        divisorsSum = getProperDivisors(num, knownProperDivisiors, primes).divisorsSum
        if divisorsSum < upToNbr and num != divisorsSum and num == getProperDivisors(divisorsSum, knownProperDivisiors, primes).divisorsSum:
            sum += num + divisorsSum

    return sum / 2
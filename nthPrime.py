import math

def isPrime(n):
    upperBound = math.floor(math.sqrt(n)) + 1
    
    for i in range(2, int(upperBound)):
        if n % i == 0:
            return False

    return True

def nthPrime(n):
    curNum = 5
    primesFound = 4
    while(True):
        curNum = curNum + 6
        if(isPrime(curNum)):
            primesFound = primesFound + 1
            if(primesFound < n):
                break
        curNum = curNum + 2
        if(isPrime(curNum)):
            primesFound = primesFound + 1
            if(primesFound < n):
                break

    return curNum
        

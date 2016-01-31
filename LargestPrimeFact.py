import math

def isPrime(n):
    if n < 2:
        return False
    
    upperBound = math.floor(math.sqrt(n)) + 1
    
    for i in range(2, int(upperBound)):
        if n % i == 0:
            return False

    return True


curFactor = 2
num = 600851475143
upperBound = int(math.floor(math.sqrt(num)) + 1)

while(curFactor < num):
    if(isPrime(curFactor)):
        while(num % curFactor == 0):
            print curFactor
            num = num / curFactor
    curFactor = curFactor + 1

print curFactor
            

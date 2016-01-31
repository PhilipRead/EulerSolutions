
primes = [2, 3, 5, 7, 11, 13, 17, 19]
maxNum = 20

totalProduct = reduce(lambda x,y : x*y, primes)

for prime in primes:
    product = prime * prime
    if(product > maxNum):
        break
    while(True):
        totalProduct = totalProduct * prime
        product = product * prime
        if(product > maxNum):
            break

print totalProduct


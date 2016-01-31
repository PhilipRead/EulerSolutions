def primeSum(n):
    nums = list(range(n-1, 3, -2))
    curPrime = 3
    primeSum = 2 + 3
    while(curPrime*curPrime < n):
        print(curPrime)
        removes = set(list(range(curPrime*curPrime, n, 2*curPrime)))
        numSet = set(nums)
        numSet.difference_update(removes)
        nums = list(numSet)
        nums.sort()
        nums.reverse()
        curPrime = nums.pop()
        primeSum = primeSum + curPrime

    
    return primeSum + sum(nums)

print(primeSum(2000000))

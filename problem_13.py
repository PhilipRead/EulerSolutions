from threading import Thread

numss = []

def parseNums(numStrs):
    extraDigits = len(str(len(numStrs) - 1))
    for numStr in numStrs:
        nums = []
        for numChar in reversed(numStr):
            nums.append(int(numChar))
        for i in range(extraDigits):
            nums.append(0)
        numss.append(nums)
    return numss

def sumLargeNums(nums1, nums2):
    sums = []
    carry = 0
    for (n1, n2) in zip(nums1, nums2):
        rawSum = n1 + n2 + carry
        if rawSum > 9:
            carry = 1
            sums.append(rawSum % 10)
        else:
            carry = 0
            sums.append(rawSum)
    return sums

def addingJob(nums1, nums2):
    sums = sumLargeNums(nums1, nums2)
    while(len(numss) > 0):
        sums = sumLargeNums(sums, numss.pop())
    numss.append(sums)

def digitsLeadingSum(numStrs, leadingDigitsLen):
    numss = parseNums(numStrs)
    addingJobs = []
    for i in range(len(numss)//2):
        addingJobs.append(Thread(target=addingJob, args=(numss.pop(), numss.pop())))
    for job in addingJobs:
        job.start()
    for job in addingJobs:
        job.join()
    leadingDigits = ''
    finalSums = numss[0]
    index = len(finalSums)-1
    while(True):
        if(finalSums[index] != 0):
            break
        index -= 1
    for i in range(index, index-leadingDigitsLen, -1):
        leadingDigits += str(finalSums[i])
    return leadingDigits

data = open('problem_13_data.txt')
numStrs = []
for line in data:
    numStrs.append(line.rstrip())

print(digitsLeadingSum(numStrs, 10))
    

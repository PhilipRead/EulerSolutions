from __future__ import print_function
import math

def findMillthPerm():
    numPermsLeft = 1000000
    numsLeft = range(10)
    numNumsLeft = 10

    while numNumsLeft > 1:

        nextNumPerms = math.factorial(numNumsLeft-1)
        curNumPerms = 0
        for i in numsLeft:
            if (nextNumPerms + curNumPerms) >= numPermsLeft:
                print(i, end="")
                numsLeft.remove(i)
                numPermsLeft -= curNumPerms
                break
            else:
                curNumPerms += nextNumPerms

        numNumsLeft -= 1

    print(numsLeft[0], end="")
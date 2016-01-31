def longestRecCycle():
    longestCycle = (0,0)
    curMax = 10
    while curMax <= 1000:
        for denom in range(curMax/10 + 1, curMax):
            curNumr = curMax
            foundRemainders = []
            curRem = curNumr % denom 
            while curRem != 0:
                if curRem in foundRemainders:
                    curCycleLen = len(foundRemainders) - foundRemainders.index(curRem)
                    if curCycleLen > longestCycle[1]:
                        longestCycle = (denom, curCycleLen)
                    break

                foundRemainders.append(curRem)
                curNumr = curRem * 10
                curRem = curNumr % denom
        curMax *= 10

    return longestCycle
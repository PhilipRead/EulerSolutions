import math
from decimal import Decimal, ROUND_FLOOR
PHI = Decimal((1 + 5**.5)/2)
convFib = lambda num : ((PHI**num - (Decimal(-1)/PHI)**num)/Decimal(5).sqrt()).to_integral_exact(rounding=ROUND_FLOOR)
lenFib = lambda num : int((convFib(num).log10() + 1).to_integral_exact(rounding=ROUND_FLOOR))

def find1000Num():
    curNum = 4500
    numDigits = lenFib(curNum)
    while numDigits < 1000:
        curNum += 1
        numDigits = lenFib(curNum)

    return curNum
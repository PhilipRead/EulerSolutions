import math

def numToDigitsSet(num):
    digits = set([])

    while num > 0:
        digits.add(num % 10)
        num //= 10

    return digits

def isPang(product, multiDigits):
    if int(math.log10(product)) + 1 == 5:
        return False

    productDigits = numToDigitsSet(product)

    if len(productDigits) < 4:
        return False

    for num in productDigits:
        if num == 0 or num in multiDigits:
            return False
    return True

def get1By4s():
    pangProducts = set([])

    for d1 in range(1, 10):
        for d2 in [i for i in range(1, 10) if i != d1]:
            for d3 in [i for i in range(1, 10) if i not in [d1, d2]]:
                for d4 in [i for i in range(1, 10) if i not in [d1, d2, d3]]:
                    for d5 in [i for i in range(1, 10) if i not in [d1, d2, d3, d4]]:
                        curProduct = d1 * (d2 * 1000 + d3 * 100 + d4 * 10 + d5)
                        if isPang(curProduct, [d1, d2, d3, d4, d5]):
                            pangProducts.add(curProduct)

    return pangProducts;

def get2By3s():
    pangProducts = set([])

    for d1 in range(1, 10):
        for d2 in [i for i in range(1, 10) if i != d1]:
            for d3 in [i for i in range(1, 10) if i not in [d1, d2]]:
                for d4 in [i for i in range(1, 10) if i not in [d1, d2, d3]]:
                    for d5 in [i for i in range(1, 10) if i not in [d1, d2, d3, d4]]:
                        curProduct = (d1 * 10 + d2) * (d3 * 100 + d4 * 10 + d5)
                        if isPang(curProduct, [d1, d2, d3, d4, d5]):
                            pangProducts.add(curProduct)
    return pangProducts;

def getPangProducts():
    pangProducts = set([])
    pangProducts.update(get1By4s())
    pangProducts.update(get2By3s())
    return sum(pangProducts)
                        
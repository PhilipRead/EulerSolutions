import heapq

class ProductTuple:
    def __init__(self, _fact1, _fact2):
        self.product = _fact1 * _fact2 * -1
        self.fact1 = _fact1
        self.fact2 = _fact2
    def __cmp__(self, other):
        return cmp(self.product, other.product)

def addNextProds(heap, fact, topBound):
    if(fact == 0): return
    for i in xrange(fact, topBound+1):
        heapq.heappush(heap, ProductTuple(fact, i))

def isPalindrome(num):
    numStr = str(num)
    if(numStr == numStr[::-1]):
        return True
    else:
        return False

lowerFact = 999
upperFact = 999
prodHeap = []

prodHeap.append(ProductTuple(upperFact, upperFact))
heapq.heapify(prodHeap)

while(len(prodHeap) > 0):
    nextMax = heapq.heappop(prodHeap)
    nextProd = nextMax.product * -1
    if(isPalindrome(nextProd)):
        print '{0} * {1} = {2}'.format(nextMax.fact1, nextMax.fact2, nextProd)
        break
    if(nextMax.fact1 == lowerFact):
        lowerFact = lowerFact - 1
        addNextProds(prodHeap, lowerFact, upperFact)



multiples = set()

curFive = 5
while(curFive < 1000):
    multiples.add(curFive)
    curFive = curFive + 5

curThree = 3
while(curThree < 1000):
    multiples.add(curThree)
    curThree = curThree + 3

sum = 0
for multiple in multiples:
    print multiple
    sum = sum + multiple

print sum



x = 1
y = 1
z = 2
evenSum = 0

while z < 4000000:
    evenSum = evenSum + z

    x = z + y
    y = x + z
    z = y + x

print evenSum

    

     

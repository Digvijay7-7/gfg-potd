result = []
for i in range(10000):
    for j in range(10000):
        if (i+j)%11 ==0:
            result.append((i,j))

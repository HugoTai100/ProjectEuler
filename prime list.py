from datetime import datetime
startTime = datetime.now()
trueprime=[]
primelist = [True] * 1000000

no = 0
for x in range(2, int(len(primelist) ** 0.5) + 1):
    if primelist[x]:
        for i in range(x+x, len(primelist), x):
            primelist[i] = False
for y in range(2,1000000):
    if primelist[y]:
        trueprime.append(y)

print (datetime.now() - startTime)


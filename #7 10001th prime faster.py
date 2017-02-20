from datetime import datetime
startTime = datetime.now()
primelist = [True] * 150000
no = 0
for x in range(2, int(len(primelist) ** 0.5) + 1):
    if primelist[x]:
        for i in range(x+x, len(primelist), x):
            primelist[i] = False
for y in range(2,150000):
    if primelist[y]:
        no = no + 1
        if no == 1:
            print(y,no)

 
print (datetime.now() - startTime)

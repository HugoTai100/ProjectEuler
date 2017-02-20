from datetime import datetime
startTime = datetime.now()
trueprime=[]
primelist = [True] * 1000000


for x in range(2, int(len(primelist) ** 0.5) + 1):
    if primelist[x]:
        for i in range(x+x, len(primelist), x):
            primelist[i] = False
for y in range(2,1000000):
    if primelist[y]:
        trueprime.append(y)
print(len(trueprime))
def ifcontaineven(num):
    for c in range(0,9,2):
        if str(c) in num: return True;
    return False;

for i in range(0,78498):
    if ifcontaineven(str(trueprime[i])):
                     
                     trueprime[i]='9'
print(len(trueprime)-trueprime.count('9'))
print(datetime.now() - startTime)

        

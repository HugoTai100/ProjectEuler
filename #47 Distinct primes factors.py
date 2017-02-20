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
def noprime(x):
    no = 0
    for i in range(0,78498):
        if x % trueprime[i] ==0:
            no = no+1
            while x % trueprime[i] == 0:
                x = x / trueprime[i]
        if x % trueprime[i]==x:
            break
    return no
th = 0
for xxx in range(1,140000):
    if th == 4:
        break

    elif noprime(xxx) ==4:
        th = th + 1
    else:
        th = 0
print(xxx-4)   
print(noprime(int(200560490130)))
      
print(datetime.now() - startTime)

        

trueprime=[]
primelist = [True] * 1000000


for x in range(2, int(len(primelist) ** 0.5) + 1):
    if primelist[x]:
        for i in range(x+x, len(primelist), x):
            primelist[i] = False
for y in range(2,1000000):
    if primelist[y]:
        trueprime.append(y)
suming = 0
maxprime = 0

for i in range(50,78498):
    suming = suming + trueprime[i]
    if trueprime.count(suming) and maxprime < suming:
        maxprime = suming
    if suming > 1000000:
        break
        
print(maxprime)

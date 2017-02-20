sieve = [True] * 2000000
for x in range(2, 1415):
    if sieve[x]:
        for i in range(x+x, len(sieve), x):
            sieve[i]=False 
            
print (sum(i for i in range(2, len(sieve)) if sieve[i]))

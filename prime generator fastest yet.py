from datetime import datetime
startTime = datetime.now()

def eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3, int(lim**0.5) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * int((lim - num * num - 1) / (2 * num) + 1)
    return [2] + [n for n in range(3, lim, 2) if sieve[n]]


 
print (datetime.now() - startTime)

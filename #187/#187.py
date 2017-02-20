'''
Semiprimes
Problem 187
A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
'''
rangee = int(10**8)
from math import sqrt
from datetime import datetime

startTime = datetime.now()

def Eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3, int(sqrt(lim)) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * int((lim - num * num - 1) / (2 * num) + 1)
    return [2] + [n for n in range(3, lim, 2) if sieve[n]]

# list all the primes in a listing,
prime = Eratosthenes_sieve(rangee)



print("prime list generated")
#print(prime)
print(datetime.now() - startTime)

# g is the sum of other combination

g = 0

ranging = len(prime)
#print(ranging)
for i in range(ranging):

    for k in range(i,ranging):

        if (prime[i] * prime[k]) < rangee and prime[i] < rangee**0.5:
            g += 1
        else:
            break
        #print(prime[i], prime[k])





print(g, "ans")
print(datetime.now() - startTime)

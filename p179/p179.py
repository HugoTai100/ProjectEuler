
def eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3, int(lim**0.5) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * int((lim - num * num - 1) / (2 * num) + 1)
    return [2] + [n for n in range(3, lim, 2) if sieve[n]]

primes = eratosthenes_sieve(10**7)
from tqdm import tqdm
print(len(primes))
print('generated')
def prime_factors(numbers):
    factor = []
    for i in primes:
        while numbers % i == 0:
            numbers = numbers // i
            factor.append(i)

        if numbers == 1:

            return factor


def print_factors(x):
    a = []
   #print("The factors of",x,"are:")
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
           #print(i, x//i)
            a = a + [i] + [x//i]
    if int(x**0.5) == x**0.5:
        return len(a)-1
    return len(a)

# take input from the user
#print(print_factors(25))

def no_factors(u):
    total = 1
    ux = prime_factors(u)
    seted = list(set(ux))

    for i in range(len(seted)):
        total = total * (1 + ux.count(seted[i]))

    return total
gg = 0
for i in tqdm(range(2,10**7)):
    if no_factors(i) == no_factors(i + 1):
        gg += 1
print(gg)
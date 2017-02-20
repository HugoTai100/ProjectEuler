# generate prime list

from tqdm import tqdm
def eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3, int(lim**0.5) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * int((lim - num * num - 1) / (2 * num) + 1)
    return [2] + [n for n in range(3, lim, 2) if sieve[n]]

primes = eratosthenes_sieve(1000000)


def if_circular_prime(ux):
    ux = str(ux)
    for i in range(len(ux)):
        if int(ux[i::] + ux [0: i]) not in primes:
            return False
    return True



total = 0
even = [2,4,6,8,0]

for i in tqdm(primes):

    if if_circular_prime(i):
        total += 1
        print(i)
print(total)
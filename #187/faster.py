from math import sqrt

from datetime import datetime
startTime = datetime.now()
def Eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3, int(sqrt(lim)) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * int((lim - num * num - 1) / (2 * num) + 1)
    return [2] + [n for n in range(3, lim, 2) if sieve[n]]



def bin_search(n, List):
    left = 0
    right = len(List) - 1

    while left <= right:
        midpoint = (left + right) // 2
        if List[midpoint] == n:
            return midpoint
        elif List[midpoint] > n:
            right = midpoint - 1
        else:
            left = midpoint + 1
    if n > List[midpoint]:
        return midpoint
    else:
        return (midpoint - 1)


def main():
    lim = 10 ** 8
    primes = Eratosthenes_sieve(lim // 2)
    res = 0
    print(datetime.now() - startTime)
    for n in range(bin_search(int(sqrt(lim)), primes) + 1):
        res += bin_search(int(lim / primes[n]), primes) - n + 1
    print(res)


if __name__ == '__main__':
    main()
    input('Press "Enter" to out...')

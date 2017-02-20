def do(N=10**8-1): ##Note the -1
    '''
    Find the number of semiprimes up to and including N; first determining the
    prime counts for all quotients of N and primes to the square root of N
    '''
    sqrt_N = int(N**0.5)
    V = [N // i for i in range(1, sqrt_N + 1)]
    V += range(V[-1] - 1, 0, -1)
    print(V)
    PrimePi = {i:i-1 for i in V}
    primes = []
    for p in range(2, sqrt_N + 1):
        if PrimePi[p] == PrimePi[p - 1]: continue   #composite
        primes.append(p)
        cp = PrimePi[p-1]  # number of primes smaller than p
        p2 = p*p
        for v in V:
            if v < p2: break
            PrimePi[v] -= PrimePi[v//p] - cp
    return sum([PrimePi[N//p] - PrimePi[p] + 1 for p in primes])

from datetime import datetime
startTime = datetime.now()
print(do())
print(datetime.now() - startTime)
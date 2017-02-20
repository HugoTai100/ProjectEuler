'''
def eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3, int(lim**0.5) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * int((lim - num * num - 1) / (2 * num) + 1)
    return [2] + [n for n in range(3, lim, 2) if sieve[n]]



primes = eratosthenes_sieve(10**8)
print('generated')
for i in range(len(primes)):
    primes.count(primes[i])
print('generated' , primes.count(primes[len(primes)-1]))
def prime_factors(numbers):
    factor = []
    for i in primes:
        while numbers % i == 0:
            numbers = numbers // i
            factor.append(i)

        if numbers == 1:

            return factor

working_no = prime_factors(60)

for i in range(len(working_no)):
    for j in range(i+1,len(working_no)):
        print(working_no[i] * working_no[j])


'''

def print_factors(x):
    a = []
   #print("The factors of",x,"are:")
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
           #print(i, x//i)
            a = a + [i] + [x//i]
    return a

# take input from the user
#print(print_factors(25))

for i in range(10**5):
    print_factors(i)

print('done')

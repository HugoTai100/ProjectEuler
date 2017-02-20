from datetime import datetime
import test_prime
startTime = datetime.now()
x = 0
prime = 2
xxx = int(input("the sum of all the primes below "))
while prime <= xxx:
    if test_prime.test(prime) == True:
        x = prime + x
        
        prime = prime + 1
    else:
        prime = prime + 1
        
    

        
print(x)
print (datetime.now() - startTime)
xxxx = input("press enter to exit")


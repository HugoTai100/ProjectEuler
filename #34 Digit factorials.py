fact  = [1,1,2,6,24,120,720,5040,40320,362880]

def sumfact(n):
    s=0
    while n > 1:
        d = int(n%10)
        
        s=s+fact[d]
        n=n/10
    return s
supersum =0
for i in range(10,100000):
    if sumfact(i)==i:
        supersum = supersum + i
print(supersum)

n = 143
working = 2*n*n-n
print(working)

print((1+(1+24*working)**0.5)/6 == (1+(1+24*working)**0.5)//6 )
print((-1+(1+8*working)**0.5)/2 == (-1+(1+8*working)**0.5)/2 )
print((1+(1+24*working)**0.5)/6 )
print((1+(1+8*working)**0.5)/2 )
# starting from 144 because 143 is chosen
for i in range(144, 1000000000000000000):
    working = 2*i*i-i
    if (1+(1+24*working)**0.5)/6 == (1+(1+24*working)**0.5)//6 and (-1+(1+8*working)**0.5)/2 == (-1+(1+8*working)**0.5)/2:
        print(working)
        break
numerator_denominator= [3, 2]

import time
start = time.time()
def step(no):
    no[0] = no[0] + no[1]
    no = no[::-1]
    no[0] = no[0] + no[1]
    return no

g = 0
for i in range(999):
    #print(numerator_denominator)
    numerator_denominator = step(numerator_denominator)
    if len(str(numerator_denominator[0])) > len(str(numerator_denominator[1])):
        g += 1


print(g)
print ("time: ", time.time() - start)
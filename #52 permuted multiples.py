def digitsum(num,y):
    
    return sum([int(x)**2 for x in str(num*y)])
print(digitsum(90,8))
from datetime import datetime
startTime = datetime.now()
mini = 987654321
for i in range(1,980000):
    
    
    if digitsum(i,1) == digitsum(i,2) == digitsum(i,3) == digitsum(i,4) == digitsum(i,5) == digitsum(i,6):
        mini = i
        break
print(mini)
print (datetime.now() - startTime)
          

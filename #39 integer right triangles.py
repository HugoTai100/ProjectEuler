gd=[]
mac, end = 0, 0
no, maxno= 0, 0
from datetime import datetime
startTime = datetime.now()
for maxx in range(0,1001,2):
    
    for j in range(1,maxx):
        for k in range(j,maxx):
            
            if (k*k+j*j)**0.5 == maxx - j - k:
                no = no + 1
            
                
                
    if no > maxno:
        maxnum = maxx
        maxno = no
    no = 0
print(maxnum)
print (datetime.now() - startTime)

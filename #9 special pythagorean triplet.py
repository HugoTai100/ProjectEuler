c=0
ansa,ansb,ansc=0,0,0
for a in range(1,3200):
    if ansa > 0:
        break
    for b in range(1,3200):
        
        if (a*a+b*b)**0.5 + a + b == 1000:
            ansa = a
            ansb = b
            ansc = (a*a+b*b)**0.5
        
print(ansa,ansb,ansc)       
print(ansa*ansb*ansc)  

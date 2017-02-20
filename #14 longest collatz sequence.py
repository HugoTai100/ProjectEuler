maxno, maxturn = 0,0
test = []
for i in range(1,1000000):
    test.append(i)
test.sort(reverse=True)

for i in range(1,len(test)):
    i = test[i]
    x=int(i)
    no = 0
    print(i)
    while i  != 1:
        
        if i%2 == 0:
             i = i/2
             if i < 1000000:
                 test.remove(i)
        else:
            i = 3*i+1
            if i < 1000000:
                 test.remove(i)
        no = no + 1
    if no > maxturn:
        maxturn = no
        maxno = x
    if i ==2:
        break
print(maxturn+1,maxno)




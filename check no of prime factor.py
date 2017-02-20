def xprime(xx):
    primelist = [True] * 150000
    no = 0
    for x in range(2, int(len(primelist) ** 0.5) + 1):
        if primelist[x]:
            for i in range(x+x, len(primelist), x):
                primelist[i] = False
    for y in range(2,150000):
        if primelist[y]:
             no = no + 1
             if no == xx:
                 return y
                
def checknodiv(x):
    th = 1
    div = 2
    end = 0
    divlist = []
    for xxx in range(1,13848):
        print(xxx)
        
for i in range(1,100):
    print(xprime(i))

       

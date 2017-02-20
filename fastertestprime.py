prime = ['2', '3']
while 2000000 > int(prime[len(prime)-1]):
    for testnoprime in range(0,int(prime[len(prime)-1])):
        if int(prime[1])%int(prime[testnoprime]) == 0:
            print('False')
        else:
            print('True') 
    
    

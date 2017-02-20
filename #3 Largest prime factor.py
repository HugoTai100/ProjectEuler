x=int(input("Input your number which its biggest prime factor is to be found "))
div = 2
bigdiv= 1
divlist = []
while (x > 1):
        if  x%div> 0:
                div = div + 1        
        else:
                x = x/div
                divlist.append(div)
                if (bigdiv < div):
                        bigdiv = div
                else:
                        bigdiv = bigdiv
                        div = 2
        
divcount = 0
start = 0
while divcount < 3:
        if len(divlist)-start == 0:
                break
        elif divlist.count(divlist[start]) >= 1:
                print('here',start)
                divcount = divcount +1
                start = divlist.count(divlist[start])
                
        

print(divcount)
print (" ")
print ('The biggest prime is ',bigdiv)
print (divlist)        
input('Press ENTER to exit')    

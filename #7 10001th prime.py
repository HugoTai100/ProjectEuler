end = int(input("the xth prime"))
end = end + 1
x = 2
div = 2
doing = 1



    
while div < x + 1 and end > doing:
    if x/div-int(x/div) == 0 and x == div:
        
        div = 2
        doing = doing + 1
        x = x + 1
    elif x/div-int(x/div)== 0 and x > div:
        
        div = 2
        x = x + 1
       
    else:
        div = div + 1
x = x - 1
print(x)
x = input("Press ENTER to end")

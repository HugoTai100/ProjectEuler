from datetime import datetime
startTime = datetime.now()
import math
yy = input("Press Enter to start searching for largest palindrome product")
x=100
y=99
result = 0
digits = 0
gdresult = 0
while x < 1000:
    while y < 999:
        y = y + 1
        uuu = x*y
        ttt = str(uuu)
        result = [ttt]
        # check if palindrome
        
        digits = len(result)
        first = result[0]
        firstto2 = 1
        second = result[1]
        secondto3 = 1
        third = result[2]
        thirdto4 = 1
        fourth = result[3]
        fourthto5 = 1
        fifth = result[4]
        if digits == 6:
            fifthto6 = result[5]
            sixth = result[5]
            if first == sixth and second == fifth and third == fourth and result > gdresult:
                gdresult = result
                gy=y
                gx=x
        else:
            if first ==fifth and second ==fourth and result > gdresult:
                gdresult = result
                gy=y
                gx=x
    
    
    y=99
    x=x+1
print(gx)
print(gy)
print(gdresult)
print ("time used", datetime.now() - startTime)
input("Press ENTER to Exit")
    
       
    
    
    

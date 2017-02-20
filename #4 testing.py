import math

result = int(input("your munber"))
gdresult = 0
digits = int(math.log10(result))+1
first = int(result/math.pow(10,(digits-1)))
firstto2 = int(result - first*math.pow(10,(digits-1)))
second = int(firstto2/math.pow(10,(digits-2)))
secondto3 = int(firstto2 - second*math.pow(10,(digits-2)))
third = int(secondto3/math.pow(10,(digits-3)))
thirdto4 = int(secondto3 - third*math.pow(10,(digits-3)))
fourth = int(thirdto4/math.pow(10,(digits-4)))
fourthto5 = int(thirdto4 - fourth*math.pow(10,(digits-4)))
fifth = int(fourthto5/math.pow(10,(digits-5)))
if digits == 6:
    fifthto6 = int(fourthto5 - fifth*math.pow(10,(digits-5)))
    sixth = int(fifthto6/math.pow(10,(digits-6)))
    if first == sixth and second == fifth and third == fourth and result > gdresult:
        gdresult = result

    else:
        gdresult = gdresult
else:
    if first ==fifth and second ==fourth and result > gdresult:
        gdresult = result
    else:
        gdresult = gdresult
        
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
if digits ==6:
    print(sixth)
    
print(gdresult)

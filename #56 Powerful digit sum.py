def digitsum(num):
    return sum(map(int,str(num)))
power, superpower = 0,0
for i in range(0,101):
    for j in range(0,101):
        power = digitsum(i**j)
        if power > superpower:
            superpower = power
print(superpower)

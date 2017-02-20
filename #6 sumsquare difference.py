number = int(input("Input your number:\n"))
a=1
b=0
while a <number+1:
    b=a*a+b
    a=a+1
print(int(b))

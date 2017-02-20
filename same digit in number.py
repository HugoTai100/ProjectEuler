def ifsamedigit(num):
    number=[]
    for x in str(num):
        number.append(x)
    if len(set(number)) == len(number):
        return False
    else:
        return True
        print(number)


print(ifsamedigit(677))


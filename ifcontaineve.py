def ifcontaineven(num):
    for c in range(0,9,2):
        if str(c) in num: return True;
    return False;
print(ifcontaineven('135079'))

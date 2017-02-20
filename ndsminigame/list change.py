kk = ["you", "car"]

def change(list):
    uu = list[:]
    uu[1] = 'fuck'
    return uu
dd = change(kk)
print(dd ,"car")
print(kk)


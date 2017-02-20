#x = int(input("input a number: "))


def no_of_recurring(test):
    ans = []
    ansfin = []
    for i in range(test):
        modans = (10 ** i) % test
        ans.append(modans)
        if ans.count(modans) == 2:
            ansfin = [i for i in range(len(ans)) if ans[i] == modans]
            break
        else:
            continue
    return int(ansfin[1]-ansfin[0])
    ansfin=[]
    ans=[]

#print(no_of_recurring(x))
maxr = 0
maxno = 0

hugo =[]

for i in range(3,1000):

    hugo.append(no_of_recurring(int(i)))

# the 3 is for error correction for the list anding the 3 to the listing
print(hugo.index(max(hugo))+3)

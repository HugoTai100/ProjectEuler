from itertools import permutations
list2={}
listt = []
for p in permutations('0123456789',10):
    listt.append(''.join(p))

# check /17 at xxxxxx123

for j in range(len(listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[7:10])%17 != 0:
        listt.pop(j)
print(len(listt))
# check /13 at xxxxx123x

for j in range(len(listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[6:9])%13 != 0:
        listt.pop(j)
print(len(listt))
# check /11 at xxxxx123x

for j in range(len(listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[5:8])%11 != 0:
        listt.pop(j)
print(len(listt))
# check /7 at xxxxx123x

for j in range(len(listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[4:7])%7 != 0:
        listt.pop(j)
print(len(listt))        
# check /5 at xxxxx123x

for j in range(len( listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[3:6])%5 != 0:
        listt.pop(j)
print(len(listt))
# check /3 at xxxxx123x

for j in range(len(listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[2:5])%3 != 0:
        listt.pop(j)
print(len(listt))
# check /2 at xxxxx123x

for j in range(len(listt)-1,-1,-1):
    tempnum = listt[j]
    if int(tempnum[1:4])%2 != 0:
        listt.pop(j)
print(len(listt))
listtt=[]
for i in listt:
    listtt.append(int(i))
print(sum(listtt))


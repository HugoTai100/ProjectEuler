from datetime import datetime
startTime = datetime.now()
ans=[]
for a in range(2,101):
    for b in range(2,101):
        tm = a**b
        if ans.count(tm) == 0:
            ans.append(a**b)
print(len(ans))
print(datetime.now() - startTime)

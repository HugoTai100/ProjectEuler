import datetime as d

date = d.date(1900, 1, 1).isoweekday()


print(date)
g = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if d.date(i, j, 1).isoweekday() == 7:
            g += 1
print(g)
listing = []

for k in range(2,1000000):
    summ = 0
    for i in str(k):
        summ += int(i) ** 5
    if summ == k:
        listing.append(k)
        print(listing)
    else:
        continue

un = 0
for i in listing:
    un += i
print(un)
summ = 0

for i in range(1,1000001):
    if str(i) == str(i)[::-1] and bin(i)[2::] == bin(i)[2::][::-1]:
        summ += i
print(summ)


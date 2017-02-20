
namee = "io"+"hu"

print(namee[3])
print(len(namee))


listt = -1
word = ""

while len(word) < 1000005:
    listt += 1
    word += str(listt)

summ = 1
for i in range(7):
    summ = summ * int(word[10**i])

print(summ)
keys = [
    319,
    680,
    180,
    690,
    129,
    620,
    762,
    689,
    762,
    318,
    368,
    710,
    720,
    710,
    629,
    168,
    160,
    689,
    716,
    731,
    736,
    729,
    316,
    729,
    729,
    710,
    769,
    290,
    719,
    680,
    318,
    389,
    162,
    289,
    162,
    718,
    729,
    319,
    790,
    680,
    890,
    362,
    319,
    760,
    316,
    729,
    380,
    319,
    728,
    716]

keys = list(set(keys))
def match(namee, check):
    if namee.count(check[0]) == 1 and namee.count(check[1]) == 1 and namee.count(check[2]) == 2:
        return namee.index(check[0]) < namee.index(check[1]) < namee.index(check[2])
    else:
        return False


print(match("1239976", "136"))
'''
namee = "hugo"
check = 'hug'

print(keys[9])
print(len(keys))

for i in range(123,10**8):
    for k in keys:
        if match(str(i),str(k)):

            break

        else:
            break

print('done')


'''
def digitsum(num):
    return sum(int(x)**2 for x in str(num))

print(digitsum(67))

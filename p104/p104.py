def next_fibonacci(first, second):
    return first + second
nth = 2


from tqdm import tqdm
first = 1
second = 1
third = 1

def lastt(number):
    number = number % 1000000000
    number = str(number)

    if ''.join(sorted(number)) == '123456789':
        return True

def firstt(number):
    number = str(number)

    if ''.join(sorted(number[0:9])) == '123456789':
        return True

for i in range(1048415641684512384512384513):
    third = next_fibonacci(first, second)
    first = second
    second = third
    nth += 1
    if len(str(third)) == 18:
        break


for i in tqdm(range(210587032341446)):
    third = next_fibonacci(first, second)
    first = second
    second = third
    nth += 1
    if firstt(third) and lastt(third):
        break



print(len(str(third)), nth)

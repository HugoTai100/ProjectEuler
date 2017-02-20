import math as mm
from tqdm import tqdm
from time import sleep


def next_term(position, summm):
    return int(summm + mm.gcd(position + 1, summm))

def skip(position, summm, maxrange):
    newpost = position * 2 - 1
    if maxrange < newpost:
        return False
    for i in range(position, position + 1000):
        if next_term(i, summm) == 3 * (i + 1):
            return False
        else:
            summm = next_term(i, summm)

    else:
        return True

def gn(n):

    summ = 13
    working = 4

    for i in range(5, 10000000000000000):
        if working == n:
            return summ
        #print(working, summ)
        if skip(working, summ, n):
            working = working * 2 -1
            summ = working * 3


        else:

            summ = next_term(working, summ)
            working += 1



print(gn(10**8))
print('breaking')
print(skip(4,13,6548418))
print(next_term(4,13))
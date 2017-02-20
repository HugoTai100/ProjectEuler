import math


def GetDigits(n):
    Digits = [];
    while n > 0:
        Digits.append(n % 10);
        n = int(n / 10);
    return Digits;


def Solve():
    a, b = 0, 1;
    i = 2;

    Phi = (1 + math.sqrt(5)) / 2;

    while True:
        c = (a + b) % (10 ** 9);
        a, b = b, c;

        if i % 1000 == 0:
            print(i);

        LastDigits = GetDigits(c);
        LastDigits.sort();
        if LastDigits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Fib(", i, ") - ", "Last digits ok");
        else:
            i = i + 1;
            continue;

        LogFib = i * math.log(Phi, 10) - math.log(math.sqrt(5), 10);
        d = int(pow(10, LogFib - int(LogFib - 8)));

        FirstDigits = GetDigits(d);
        FirstDigits.sort();
        if FirstDigits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Fib(", i, ") - ", "First digits ok");
        else:
            i = i + 1;
            continue;

        break;

    print("\n\n\nSolution : Fib(", i, ")", );


print("PROJECT EULER 104:");
Solve();

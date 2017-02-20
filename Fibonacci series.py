def fib(n):
    a, b = 1, 1
    ans = 0
    while a < n:
        
        a, b = b, a+b
        if a % 2 == 0:
            ans = a +ans
    print(ans)
fib(4000000)


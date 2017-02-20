def is_prime(num):
    if num ==0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
        else:
            return True
print [x for x in range(2,100) if not [t for t in range(2,x) if not x%t]]

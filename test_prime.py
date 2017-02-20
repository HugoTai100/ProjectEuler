def test(x):
    div = 2
    while div < x + 1:
        if x%div == 0 and x== div:
            
            return True
            break
        elif x%div == 0 and x > div:
            return False
        else:
            div = div + 1
print(test(2))



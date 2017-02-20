import p443

pp=1000


summ = 13
for i in range(5, pp):
    summ = p443.next_term(i-1, summ)
    print(i, summ)


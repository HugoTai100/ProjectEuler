def print_puzzle(puzzle_size, size):
    for i in range(size):
        print(puzzle_size[size * i:(i + 1) * size])


def turn(piece):
    if piece:
        return 0
    else:
        return 1


def turn_batch(no, list):
    list1 = list[:]
    for i in no:
        list1[i] = turn(list[i])
    return list1


def group_turn(place, size, settt):
    sett = settt[:]
    '''vertex change'''
    '''top left'''
    if place == 1:
        turn_batch([0, 1, size, size + 1], sett)
        ''' '''
    elif place == size:
        turn_batch([place - 2, place - 1, place + size - 2, place + size - 1], sett)
    elif place == size * size - size + 1:
        turn_batch([size * (size - 2), size * (size - 2) + 1, size * (size - 1), size * (size - 1) + 1], sett)
    elif place == size * size:
        turn_batch([size * size - 1, size * size - 2, size * size - size - 1, size * size - size - 2], sett)
        '''edge change'''
    elif 0 < place < size:
        turn_batch([place - 1, place, place - 2, place - 1 + size, place + size, place - 2 + size], sett)
    elif size * size >= place > size * size - size:
        turn_batch([place - 1, place - 2, place, place - 1 - size, place - 2 - size, place - size], sett)
    elif place % size == 0:
        turn_batch([place - 1, place - 1 - size, place - 1 + size, place - 2, place - 2 - size, place - 2 + size], sett)
    elif (place - 1) % size == 0:
        place = place + size
        turn_batch([place - 1 - (size - 1), place - 1 - size - (size - 1), place - 1 + size - (size - 1),
                    place - 2 - (size - 1), place - 2 - size - (size - 1), place - 2 + size - (size - 1)], sett)
    else:
        turn_batch([place - 1, place - 2, place, place - 1 + size, place - 2 + size, place + size, place - 1 - size,
                    place - 2 - size, place - size], sett)
    return sett

def change_to_list(noo):
    aa = []
    noo = str(noo)
    for i in noo:
        aa.append(int(i))
    return aa


def solve(b4, after, size):
    for i in range(len(b4)):
        (print(group_turn(5, size, b4)))

        if group_turn(i, size, b4) == after:
            return i + 0


def print_grid(a_list, grid_name):
    str_list = []
    for i in a_list:
        str_list.append(str(i))

    size = int(len(a_list) ** 0.5)
    print("==", str(grid_name), "==")
    for i in range(size):
        print(''.join((str_list[i * size: (i + 1) * size])))


size = int(input("Puzzle size: "))


def solve(size, before, after1):
    doing = []
    ddd = 0
    before_use = before

    for i in range(size * size):
        print_grid(before_use, "before")
        print("=========", ddd)
        print_grid(after1, "after1")
        doing = group_turn(ddd, size, before_use)
        if after1 == doing:
            print_grid(doing)
            print("this is set", ddd, after1 == doing)
            return ddd

        else:
            ddd += 1
            before_use = before
            print_grid(before, "before")
            print_grid(before_use, "before use")
            print('-----')


before12 = [1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1]

after12 = [1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1]

print('Starts')
print(solve(size, before12, after12))

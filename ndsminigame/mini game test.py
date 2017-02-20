def turn(piece):
    if piece:
        return 0
    else:
        return 1


def turn_batch(no, list1):
    list2 = list1[:]
    for i in no:
        list2[i] = turn(list2[i])
    return list2


def group_turn(place, settt):
    sett = settt[:]
    size = int(len(sett) ** 0.5)
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
        place += size
        turn_batch([place - 1 - (size - 1), place - 1 - size - (size - 1), place - 1 + size - (size - 1),
                    place - 2 - (size - 1), place - 2 - size - (size - 1), place - 2 + size - (size - 1)], sett)
    else:
        turn_batch([place - 1, place - 2, place, place - 1 + size, place - 2 + size, place + size, place - 1 - size,
                    place - 2 - size, place - size], sett)
    return sett


def print_grid(a_list, grid_name):
    str_list = []
    for i in a_list:
        str_list.append(str(i))

    size = int(len(a_list) ** 0.5)
    print("==", str(grid_name), "==")
    for i in range(size):
        print(''.join((str_list[i * size: (i + 1) * size])))


after12 = [1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1]

gg = group_turn(3, after12)
xx = gg

dd = group_turn(4, gg)

for i in range(1, 26):
    print_grid(group_turn(i, after12), i)
    print(group_turn(i, after12))



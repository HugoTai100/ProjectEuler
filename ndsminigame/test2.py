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
    if place == 0:
        return sett
    if place == 1:
        sett = turn_batch([0, 1, size, size + 1], sett)
        ''' '''
    elif place == size:
        sett = turn_batch([place - 2, place - 1, place + size - 2, place + size - 1], sett)
    elif place == size * size - size + 1:
        sett = turn_batch([size * (size - 2), size * (size - 2) + 1, size * (size - 1), size * (size - 1) + 1], sett)
    elif place == size * size:
        sett = turn_batch([size * size - 1, size * size - 2, size * size - size - 1, size * size - size - 2], sett)
        '''edge change'''
    elif 0 < place < size:
        sett = turn_batch([place - 1, place, place - 2, place - 1 + size, place + size, place - 2 + size], sett)
    elif size * size >= place > size * size - size:
        sett = turn_batch([place - 1, place - 2, place, place - 1 - size, place - 2 - size, place - size], sett)
    elif place % size == 0:
        sett = turn_batch(
            [place - 1, place - 1 - size, place - 1 + size, place - 2, place - 2 - size, place - 2 + size], sett)
    elif (place - 1) % size == 0:
        place += size
        sett = turn_batch([place - 1 - (size - 1), place - 1 - size - (size - 1), place - 1 + size - (size - 1),
                           place - 2 - (size - 1), place - 2 - size - (size - 1), place - 2 + size - (size - 1)], sett)
    else:
        sett = turn_batch(
            [place - 1, place - 2, place, place - 1 + size, place - 2 + size, place + size, place - 1 - size,
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


def solve(before_list, after_list):
    ranging = len(before_list) + 1
    for k in range(0, ranging):

        changed3 = group_turn(k, before_list)
        for j in range(0, ranging):

            changed0 = group_turn(j, changed3)
            for i in range(0, ranging):
                changed1 = group_turn(i, changed0)
                if changed1 == after_list:
                    return i, j, k
    return "Error"


def change_to_list(strr):
    griding =[]
    for i in str(strr):
        griding.append(int(i))
    return griding

after12 = [1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1,
           1, 1, 1, 1, 1]

after123 = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

before12 = [1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 1, 1, 0,
            1, 0, 1, 1, 0,
            1, 1, 0, 0, 0]

testgrid_4x4 = [1, 0, 0, 1,
                1, 1, 0, 1,
                1, 0, 1, 1,
                1, 0, 0, 1]

testgrid_4x4_2 = [1] * 16
two    = 100110110111001
square = '0000011001100000'
fivexfive = "0101010101010101010101010"
sixsix = "010101101010010101101010010101101010"
six2   = "100001110001101001100101100011100001"
grid_2 = [1, 0, 0, 1,
          1, 1, 0, 1,
          1, 0, 1, 1,
          1, 0, 0, 1]

print(solve(change_to_list(input("before list: ")), change_to_list(input("after list:  "))))



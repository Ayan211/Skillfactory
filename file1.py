pole = [[' ', 1, 2, 3],
        [1, '-', '-', '-'],
        [2, '-', '-', '-'],
        [3, '-', '-', '-']]


def pole_print():
    for i in range(4):
        for j in range(4):
            print(pole[i][j], end=' ')
        print()


def check(player):
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            if pole[i][j] != player:
                break
            elif j == 3:
                return True
    for j in [1, 2, 3]:
        for i in [1, 2, 3]:
            if pole[i][j] != player:
                break
            elif i == 3:
                return True
    if pole[1][1] == player == pole[2][2] == pole[3][3]:
        return True
    if pole[1][3] == player == pole[2][2] == pole[3][1]:
        return True


def vvod(player):
    print("ход игрока '%s'" % player)
    print("введите координаты ")
    a = input('вертикальные от 1 до 3: ')
    b = input('горизонтальные от 1 до 3: ')
    if (a in ('1', '2', '3')) and (b in ('1', '2', '3')):
        a = int(a)
        b = int(b)
        if pole[a][b] == '-':
            pole[a][b] = player
            return False
        else:
            print("клетка занята")
            return True
    else:
        print("ошибка координат")
        return True


for i in range(9):
    if (i+1) % 2 == 1:
        player = 'x'
    else:
        player = 'o'
    pole_print()
    while vvod(player):
        True
    if check(player):
        pole_print()
        exit(print("победа игрока '%s'" % player))
    elif i+1 == 9:
        print("ничья")

a = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print('---------')
print('| ' + a[0] + ' ' + a[1] + ' ' + a[2] + ' |')
print('| ' + a[3] + ' ' + a[4] + ' ' + a[5] + ' |')
print('| ' + a[6] + ' ' + a[7] + ' ' + a[8] + ' |')
print('---------')

WW = [[a[0], a[1], a[2]],
      [a[3], a[4], a[5]],
      [a[6], a[7], a[8]]]

for num in a:
    for x in num:
        coord = input('Enter the coordinates:')
        if (coord[0].isdigit()) and coord[2].isdigit():
            coord_1 = int(coord[0])
            coord_2 = int(coord[2])
            i = coord_1 - 1
            j = coord_2 - 1
            if (coord_1 >= 4) or (coord_2 >= 4):
                print('Coordinates should be from 1 to 3!')
            elif (WW[i][j] == 'X') or (WW[i][j] == 'O'):
                print('This cell is occupied! Choose another one!')
            else:
                WW[i][j] = 'X'
                print('---------')
                print('| ' + " ".join(WW[0]) + ' |')
                print('| ' + " ".join(WW[1]) + ' |')
                print('| ' + " ".join(WW[2]) + ' |')
                print('---------')
        else:
            print('You should enter numbers!')

    N = [[WW[0][0], WW[1][0], WW[2][0]], [WW[0][1], WW[1][1], WW[2][1]], [WW[0][2], WW[1][2], WW[2][2]]]
    A = [[WW[0][2], WW[1][1], WW[2][0]], [WW[0][0], WW[1][1], WW[2][2]]]
    x_0 = WW[0].count('X')
    x_1 = WW[1].count('X')
    x_2 = WW[2].count('X')
    x_3 = N[0].count('X')
    x_4 = N[1].count('X')
    x_5 = N[2].count('X')
    x_6 = A[0].count('X')
    x_7 = A[1].count('X')
    y_0 = WW[0].count('O')
    y_1 = WW[1].count('O')
    y_2 = WW[2].count('O')
    y_3 = N[0].count('O')
    y_4 = N[1].count('O')
    y_5 = N[2].count('O')
    y_6 = A[0].count('O')
    y_7 = A[1].count('O')
    L = WW[0].count(' ')
    L_1 = WW[1].count(' ')
    L_2 = WW[2].count(' ')
    X = (x_0 == 3) or (x_1 == 3) or (x_2 == 3) or (x_3 == 3) or (x_4 == 3) or (x_5 == 3) or (x_6 == 3) or (x_7 == 3)
    Y = (y_0 == 3) or (y_1 == 3) or (y_2 == 3) or (y_3 == 3) or (y_4 == 3) or (y_5 == 3) or (y_6 == 3) or (y_7 == 3)
    if (X is True) and (Y is False):
        print('X wins')
        break
    elif Y is True and (X is False):
        print('O wins')
        break
    elif (Y is False) and (X is False) and ((L == 0) and (L_1 == 0) and (L_2 == 0)):
        print('Draw')
        break

    for o in num:
        coord_o = input('Enter the coordinates:')
        if (coord_o[0].isdigit()) and coord_o[2].isdigit():
            coord_1 = int(coord_o[0])
            coord_2 = int(coord_o[2])
            i = coord_1 - 1
            j = coord_2 - 1
            if (coord_1 >= 4) or (coord_2 >= 4):
                print('Coordinates should be from 1 to 3!')
            elif (WW[i][j] == 'X') or (WW[i][j] == 'O'):
                print('This cell is occupied! Choose another one!')
            else:
                WW[i][j] = 'O'
                print('---------')
                print('| ' + " ".join(WW[0]) + ' |')
                print('| ' + " ".join(WW[1]) + ' |')
                print('| ' + " ".join(WW[2]) + ' |')
                print('---------')
        else:
            print('You should enter numbers!')
    N = [[WW[0][0], WW[1][0], WW[2][0]], [WW[0][1], WW[1][1], WW[2][1]], [WW[0][2], WW[1][2], WW[2][2]]]
    A = [[WW[0][2], WW[1][1], WW[2][0]], [WW[0][0], WW[1][1], WW[2][2]]]
    x_0 = WW[0].count('X')
    x_1 = WW[1].count('X')
    x_2 = WW[2].count('X')
    x_3 = N[0].count('X')
    x_4 = N[1].count('X')
    x_5 = N[2].count('X')
    x_6 = A[0].count('X')
    x_7 = A[1].count('X')
    y_0 = WW[0].count('O')
    y_1 = WW[1].count('O')
    y_2 = WW[2].count('O')
    y_3 = N[0].count('O')
    y_4 = N[1].count('O')
    y_5 = N[2].count('O')
    y_6 = A[0].count('O')
    y_7 = A[1].count('O')
    L = WW[0].count(' ')
    L_1 = WW[1].count(' ')
    L_2 = WW[2].count(' ')
    X = (x_0 == 3) or (x_1 == 3) or (x_2 == 3) or (x_3 == 3) or (x_4 == 3) or (x_5 == 3) or (x_6 == 3) or (x_7 == 3)
    Y = (y_0 == 3) or (y_1 == 3) or (y_2 == 3) or (y_3 == 3) or (y_4 == 3) or (y_5 == 3) or (y_6 == 3) or (y_7 == 3)
    if (X is True) and (Y is False):
        print('X wins')
        break
    elif Y is True and (X is False):
        print('O wins')
        break
    elif (Y is False) and (X is False) and ((L == 0) and (L_1 == 0) and (L_2 == 0)):
        print('Draw')
        break

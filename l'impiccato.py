import os

err = 0
matrix_s_m = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],

]
while True:
    if err >= 1:
        matrix_s_m[1][8] = '|'
    if err >= 2:
        matrix_s_m[2][8] = '0'
    if err >= 3:
        matrix_s_m[3][8] = 'I'
    if err >= 4:
        matrix_s_m[4][8] = '|'
    if err >= 5:
        matrix_s_m[5][8] = '|'
    if err >= 6:
        matrix_s_m[4][7] = '/'
    if err >= 7:
        matrix_s_m[5][7] = ''
        matrix_s_m[5][6] = ' /'
    if err >= 8:
        matrix_s_m[6][7] = ' /'
    if err >= 9:
        matrix_s_m[7][7] = '/'
    if err >= 10:
        matrix_s_m[4][9] = '\ '
    if err >= 11:
        matrix_s_m[5][9] = ''
        matrix_s_m[5][10] = '\ '
    if err >= 12:
        matrix_s_m[6][8] = '\ '
    if err >= 8:
        matrix_s_m[7][9] = '\ '
    for row in matrix_s_m:
        print(' '.join(row))

    word = input('scegli la parola con cui giocare: ').lower().strip()

    os.system('clear')
    break
    # while True:
    #     guess = input('Inserisci una lettera o la parola: ')
    #     for row in matrix_s_m:
    #         print(' '.join(row))
    #         break
    # break




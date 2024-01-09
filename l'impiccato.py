import os
from time import sleep

err = 0
l_count = 0
n = 0

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
# parola check
while True:
    word = input('Scegli la parola con cui giocare: ').lower().strip()
    is_ok = True
    n = False
    for l in word:
        l_count += 1
        try:
            isinstance(int(l), int)
            n = True
        except ValueError:
            pass
        if n:
            print('Non sono amessi numeri nella parola!')
            sleep(2)
            os.system('clear')
            is_ok = False
            break
        if l_count > 32:
            print('Dai mo, non esageriamo! \n\nMassimo 32 lettere.')
            sleep(2)
            os.system('clear')
            is_ok = False
            break
        if l == ' ':
            print('Una sola parola alla volta!\n\nNiente spazi')
            sleep(2)
            os.system('clear')
            is_ok = False
            break
    if is_ok:
        os.system('clear')
        print('Ottima scelta!\n\nOra si inizia!\n\n')
        sleep(3)
        os.system('clear')
        break
    else:
        print('Prova un altra parola.')
        sleep(2)
        os.system('clear')

screen_guess = []
for le in word:
    screen_guess += '_'
print(f'{l_count} lettere.\n')

while True:
    print(screen_guess)
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
    guess = input('Inserisci una lettera o la parola: ')
    if guess == word:
        print('you win!')
        break
    # else:
    #     for let in guess:







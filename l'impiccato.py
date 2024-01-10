import os
from time import sleep


def main():
    while True:
        word = ParolaCheck()
        ImpiccatoGame(word)
        while True:
            anw_again = input('Vuoi giocare ancora?').lower().strip()
            if anw_again == 'no':
                print('Alla prossima. 👋')
                break
                break
            elif anw_again == 'si':
                print('\n\nPerfetto, preparati!')
                sleep(2)
                os.system('clear')
                break
            else:
                print('\nScusa non ho capito, si o no?')


def ParolaCheck():
    l_count = 0
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
    return word


def ImpiccatoGame(word):
    l_count = 0
    for l in word:
        l_count += 1
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
    screen_guess = []
    for le in word:
        screen_guess += '_'
    print(f'La parola contiene {l_count} lettere.\n')
    while True:
        n = -1
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
        if err >= 13:
            matrix_s_m[7][9] = '\ '
        for row in matrix_s_m:
            print(' '.join(row))
        if err >= 13:
            print('Hai perso!')
            break
        else:
            err_check = True
            guess = input('Inserisci una lettera o la parola: ').lower().strip()
            if guess == word:
                print('\nCongratulazioni! Hai Vinto!!!\n')
                break
            else:
                for let in word:
                    n += 1
                    if guess == let:
                        screen_guess[n] = guess
                        err_check = False
                if err_check:
                    err += 1


if __name__ == '__main__':
    main()
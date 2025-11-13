import os
from time import sleep
os.environ['TERM'] = 'xterm'


def main():
    play = True
    while play:
        word = SceltaParola()
        ImpiccatoGame(word)
        while True:
            anw_again = input('Vuoi giocare ancora? ').lower().strip()
            if anw_again == 'no':
                print('\nAlla prossima. 👋')
                play = False
                break
            elif anw_again == 'si':
                print('\n\nPerfetto, preparati!')
                sleep(1)
                os.system('clear')
                break
            else:
                print('\nScusa non ho capito, si o no?')


def clear_screen():
    if os.system('clear'):
        os.system('clear')
    else:
        print('\n' * 100)


def err_check_easy(err, matrix_s_m):
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
        matrix_s_m[4][9] = '\\ '
    if err >= 11:
        matrix_s_m[5][9] = ''
        matrix_s_m[5][10] = '\\ '
    if err >= 12:
        matrix_s_m[6][8] = '\\ '
    if err >= 13:
        matrix_s_m[7][9] = '\\ '
    for row in matrix_s_m:
        print(' '.join(row))
    if err >= 13:
        return 1
    return 0


def err_check_hard(err, matrix_s_m):
    if err >= 1:
        matrix_s_m[1][8] = '|'
    if err >= 2:
        matrix_s_m[2][8] = '0'
        matrix_s_m[3][8] = 'I'
    if err >= 3:
        matrix_s_m[4][8] = '|'
        matrix_s_m[5][8] = '|'
    if err >= 4:
        matrix_s_m[4][7] = '/'
        matrix_s_m[5][7] = ''
        matrix_s_m[5][6] = ' /'
    if err >= 5:
        matrix_s_m[6][7] = ' /'
        matrix_s_m[7][7] = '/'
    if err >= 6:
        matrix_s_m[4][9] = '\\ '
        matrix_s_m[5][9] = ''
        matrix_s_m[5][10] = '\\ '
    if err >= 7:
        matrix_s_m[6][8] = '\\ '
        matrix_s_m[7][9] = '\\ '
    for row in matrix_s_m:
        print(' '.join(row))
    if err >= 7:
        return 1


def err_check_hardcore(err, matrix_s_m):
    if err >= 1:
        matrix_s_m[1][8] = '|'
        matrix_s_m[2][8] = '0'
        matrix_s_m[3][8] = 'I'
    if err >= 2:
        matrix_s_m[4][8] = '|'
        matrix_s_m[4][7] = '/'
        matrix_s_m[5][7] = ''
        matrix_s_m[5][6] = ' /'
        matrix_s_m[4][9] = '\\ '
        matrix_s_m[5][9] = ''
        matrix_s_m[5][10] = '\\ '
    if err >= 3:
        matrix_s_m[5][8] = '|'
        matrix_s_m[6][7] = ' /'
        matrix_s_m[7][7] = '/'
        matrix_s_m[6][8] = '\\ '
        matrix_s_m[7][9] = '\\ '
    for row in matrix_s_m:
        print(' '.join(row))
    if err >= 3:
        return 1


def SceltaParola():
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
                sleep(1)
                clear_screen()
                is_ok = False
                break
            if l_count >= 34:
                print('Dai mo, non esageriamo! \n\nMassimo 33 lettere.')
                sleep(1)
                clear_screen()
                is_ok = False
                break
            if l == ' ':
                print('Una sola parola alla volta!\n\nNiente spazi')
                sleep(1)
                clear_screen()
                is_ok = False
                break
        if is_ok:
            os.system('clear')
            print('Ottima scelta!\n\nOra si inizia!\n\n')
            sleep(1)
            clear_screen()
            break
        else:
            print('Prova un altra parola.')
            sleep(1)
            clear_screen()
    return word


def ImpiccatoGame(word):
    global diff
    diffs = ["easy", "hard", "hardcore"]
    dif_not_set = True
    while dif_not_set:
        print("t = tentativi")
        print("Sceglierla difficoltà tra: 'Easy' (13t) 'Hard' (7t) 'hardcore' (3t)")
        diff = input("Difficoltà --> ").lower().strip()
        for m in diffs:
            if m == diff:
                dif_not_set = False
                break
        if dif_not_set:
            print('Non ho capito, le opzioni sono solo "easy", "hard", "hardcore"\n')
    l_usate = set()
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
        print(screen_guess)
        if diff == 'easy':
            if err_check_easy(err, matrix_s_m):
                print(f"SEI MORTO!\nLa parola era '{word}'\n")
                break
        if diff == 'hard':
            if err_check_hard(err, matrix_s_m):
                print(f"SEI MORTO!\nLa parola era '{word}'\n")
                break
        if diff == 'hardcore':
            if err_check_hardcore(err, matrix_s_m):
                print(f"SEI MORTO!\nLa parola era '{word}'\n")
                break
        err_control = True
        guess = input('Inserisci una lettera o la parola: ').lower().strip()

        if guess == word:
            print('\nCongratulazioni! Hai Vinto!!!\nLa parola era " ' + word + ' "')
            break
        else:
            if guess in l_usate:
                print("\nHai già provato la lettera '" + guess + "'\nProvane un altra.\n")
                continue
            if len(guess) == 1:
                l_usate.add(guess)
            n = -1
            for let in word:
                n += 1
                if guess == let:
                    screen_guess[n] = guess
                    err_control = False
            if err_control:
                err += 1
        won = 1
        for nl in range(l_count):
            if screen_guess[nl] != word[nl]:
                won = 0
        if won:
            print('\nCongratulazioni! Hai Vinto!!!\nLa parola era " ' + word + ' "')
            break


if __name__ == '__main__':
    main()

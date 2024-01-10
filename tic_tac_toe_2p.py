def main():
    rules()
    while True:
        tictactoe_game()
        while True:
            again = input("\n\nWanna play again? ")
            if again.lower().strip() == 'yes':
                print('\n\n')
                break
            elif again.lower().strip() == 'no':
                break
                break
            else:
                print("Sorry, I only understand yes or no answer. :(")


def tictactoe_scheme(one=' ', two=' ', three=' ', four=' ', five=' ', six=' ', seven=' ', eight=' ', nine=' '):
    print(f' {one} | {two} | {three} ')
    print(('_' * 3), ('_' * 3), ('_' * 3), sep='|')
    print(f' {four} | {five} | {six} ')
    print(('_' * 3), ('_' * 3), ('_' * 3), sep='|')
    print(f' {seven} | {eight} | {nine} ')
    print((' ' * 3), (' ' * 3), (' ' * 3), sep='|')


def rules():
    tictactoe_scheme(one='1', two='2', three='3', four='4', five='5', six='6', seven='7', eight='8', nine='9')
    print("""Answer using numbers from 1 to 9,
to indicate the spot that you wanna mark.
Following the logic in the example above.

""")


def tictactoe_game():
    a = ' '
    b = ' '
    c = ' '
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = ' '
    i = ' '
    tictactoe_scheme(a, b, c, d, e, f, g, h, i)
    while True:
        while True:
            try:
                x_move = int(input('Player 1 turn:\nWhat spot do you want to mark? '))
                if x_move == 1:
                    if a == ' ':
                        a = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 2:
                    if b == ' ':
                        b = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 3:
                    if c == ' ':
                        c = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 4:
                    if d == ' ':
                        d = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 5:
                    if e == ' ':
                        e = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 6:
                    if f == ' ':
                        f = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 7:
                    if g == ' ':
                        g = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 8:
                    if h == ' ':
                        h = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif x_move == 9:
                    if i == ' ':
                        i = 'x'
                        break
                    else:
                        print("\nSpot taken already!\n")
                    break
                else:
                    print("Please answer with a nuber from 1 to 9.\n")
            except ValueError:
                print("Please answer with a nuber from 1 to 9.\n")
        tictactoe_scheme(a, b, c, d, e, f, g, h, i)
        if a == 'x' and b == 'x' and c == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif d == 'x' and e == 'x' and f == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif g == 'x' and h == 'x' and i == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif a == 'x' and e == 'x' and i == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif c == 'x' and e == 'x' and g == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif a == 'x' and d == 'x' and g == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif b == 'x' and e == 'x' and h == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif c == 'x' and f == 'x' and i == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif a == 'o' and b == 'o' and c == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif d == 'o' and e == 'o' and f == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif g == 'o' and h == 'o' and i == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif a == 'o' and e == 'o' and i == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif c == 'o' and e == 'o' and g == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif a == 'o' and d == 'o' and g == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif b == 'o' and e == 'o' and h == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif c == 'o' and f == 'o' and i == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif a != ' ' and b != ' ' and c != ' ' and d != ' ' and e != ' ' and f != ' ' and g != ' ':
            if h != ' ' and i != ' ':
                print("It's a Tie")
                break
            else:
                pass
        while True:
            try:
                o_move = int(input('Player 2 turn:\nWhat spot do you want to mark? '))
                if o_move == 1:
                    if a == ' ':
                        a = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 2:
                    if b == ' ':
                        b = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 3:
                    if c == ' ':
                        c = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 4:
                    if d == ' ':
                        d = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 5:
                    if e == ' ':
                        e = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 6:
                    if f == ' ':
                        f = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 7:
                    if g == ' ':
                        g = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 8:
                    if h == ' ':
                        h = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                elif o_move == 9:
                    if i == ' ':
                        i = 'o'
                        break
                    else:
                        print("\nSpot taken already!\n")
                else:
                    print("Please answer with a nuber from 1 to 9.\n")
            except ValueError:
                print("Please answer with a nuber from 1 to 9.\n")
        tictactoe_scheme(a, b, c, d, e, f, g, h, i)
        if a == 'x' and b == 'x' and c == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif d == 'x' and e == 'x' and f == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif g == 'x' and h == 'x' and i == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif a == 'x' and e == 'x' and i == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif c == 'x' and e == 'x' and g == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif a == 'x' and d == 'x' and g == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif b == 'x' and e == 'x' and h == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif c == 'x' and f == 'x' and i == 'x':
            print('\nPlayer1 wins!!!')
            break
        elif a == 'o' and b == 'o' and c == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif d == 'o' and e == 'o' and f == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif g == 'o' and h == 'o' and i == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif a == 'o' and e == 'o' and i == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif c == 'o' and e == 'o' and g == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif a == 'o' and d == 'o' and g == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif b == 'o' and e == 'o' and h == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif c == 'o' and f == 'o' and i == 'o':
            print('\nPlayer2 wins!!!')
            break
        elif a != ' ' and b != ' ' and c != ' ' and d != ' ' and e != ' ' and f != ' ' and g != ' ':
            if h != ' ' and i != ' ':
                print("It's a Tie")
                break
            else:
                pass


if __name__ == '__main__':
    main()

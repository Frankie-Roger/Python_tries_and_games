import random
t_played = 0
t_won = 0
t_lost = 0
t_tie = 0
print("""
  *************************************
 * Benvenuti su sasso, carta, forbice! *
  *************************************

Puoi battere il computer ?

(Per terminare il progamma inserire 'fine')
""")

while True:
    x = random.randint(1, 3)  # 1= sasso. 2= carta. 3= forbice
    # if x == 1:
    #     print("🪨")
    # elif x == 2:
    #     print("🧻")
    # elif x == 3:
    #     print("✂️")
    choice = input("\nSasso, carta o forbice: ")
    if choice.lower().strip() == 'sasso':
        if x == 1:
            print("PC ha scelto: 'sasso' ")
            print("\n Tu:   🪨  vs  🪨   :Pc \n")
            print("Hai pareggiato!")
            print("\nProva ancora")
            t_tie += 1
            t_played += 1
        if x == 2:
            print("Pc ha scelto: 'carta'")
            print("\n Tu:   🪨  vs  🧻   :Pc \n")
            print("Hai perso!  🙁")
            t_played += 1
            t_lost += 1
            print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
        if x == 3:
            print("Pc ha scelto: 'forbice' ")
            print("\n Tu:   🪨  vs  ✂️   :Pc \n")
            print("Hai vinto!  🎉🎉🎉")
            t_played += 1
            t_won += 1
            print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
    elif choice.lower().strip() == 'carta':
        if x == 1:
            print("PC ha scelto: 'sasso' ")
            print("\n Tu:   🧻  vs  🪨   :Pc \n")
            print("Hai vinto!  🎉🎉🎉")
            t_played += 1
            t_won += 1
            print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
        elif x == 2:
            print("Pc ha scelto: 'carta'")
            print("\n Tu:   🧻  vs  🧻   :Pc \n")
            print("Hai pareggiato!")
            print("\nProva ancora")
            t_tie += 1
            t_played += 1
        elif x == 3:
            print("Pc ha scelto: 'forbici' ")
            print("\n Tu:   🧻  vs  ✂️   :Pc \n")
            print("Hai perso!  🙁")
            t_played += 1
            t_lost += 1
            print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
    elif choice.lower().strip() == 'forbice' or choice.lower().strip() == 'forbici':
        if x == 1:
            print("Pc picked: 'sasso'")
            print("\n Tu:   ✂️  vs  🪨   :Pc \n")
            print("Hai perso!  🙁")
            t_lost += 1
            t_played += 1
            print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
        elif x == 2:
            print("Pc ha scelto: 'carta'")
            print("\n Tu:   ✂️  vs  🧻   :Pc \n")
            print("Hai vinto!  🎉🎉🎉")
            t_played += 1
            t_won += 1
            print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
        elif x == 3:
            print("Pc ha scelto: 'forbice' ")
            print("\n Tu:   ✂️  vs  ✂️   :Pc \n")
            print("Hai pareggiato!")
            print("\nProva ancora")
            t_tie += 1
            t_played += 1
    elif choice.lower().strip() == 'fine':
        print(f"Hai giacato {t_played} volte, vinto {t_won} volte, perso {t_lost} volte e pareggiato {t_tie} volte.")
        print("\nGrazie di aver giocato, alla prossima!\n")
        break
    else:
        print("Non ho capito... Perfavore, prova di nuovo\nLe opzioni sono: sasso, carta o forbice \n\n")
        print("Per terminare il progamma inserire 'fine'")
        print("\nprova di novo!")
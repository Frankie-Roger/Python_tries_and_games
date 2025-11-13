from tkinter import *
import random

root = Tk()
root.title('🪨  📑  ✂️')

global t_played
global t_won
global t_lost
t_played = 0
t_won = 0
t_lost = 0


def reset():
    global t_played
    global t_won
    global t_lost
    global line3
    try:
        line0.destroy()
    except NameError:
        pass
    try:
        line1.destroy()
    except NameError:
        pass
    try:
        line2.destroy()
    except NameError:
        pass
    try:
        line3.destroy()
    except NameError:
        pass
    try:
        reset_btm.destroy()
    except NameError:
        pass
    t_played = 0
    t_won = 0
    t_lost = 0
    played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
    line3 = Label(root, text=played, )
    line3.grid(column=1, row=6, padx=20, pady=20)


def play():
    global line0
    global line1
    global line2
    global line3
    global reset_btm
    global t_played
    global t_won
    global t_lost
    try:
        line0.destroy()
    except NameError:
        pass
    try:
        line1.destroy()
    except NameError:
        pass
    try:
        line2.destroy()
    except NameError:
        pass
    try:
        line3.destroy()
    except NameError:
        pass

    x = random.randint(1, 3)  # 1= rock. 2= paper. 3= scissors

    choice = choise_.get()
    choise_.delete(0, last=30)

    your_emo = ''
    pc_emo = ''
    if x == 1:
        pc_emo = '🪨'
    elif x == 2:
        pc_emo = '📑'
    elif x == 3:
        pc_emo = '✂️'
    else:
        pc_emo = 'Error'

    if choice.lower() == 'rock':
        your_emo = '🪨'
        if x == 1:
            t_played += 1
            pc_rock = "Pc picked: 'Rock' "
            line1 = Label(root, text=pc_rock,)
            line1.grid(column=1, row=4, padx=20, pady=20)
            tie = "It's a tie!"
            line2 = Label(root, text=tie)
            line2.grid(column=1, row=5, padx=20, pady=20)
            try_ = "Try again"
            line3 = Label(root, text=try_, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        if x == 2:
            pc_paper = "Pc picked: 'Paper' "
            line1 = Label(root, text=pc_paper, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            loose = "😞🙁     You loose!      🙁😞"
            line2 = Label(root, text=loose, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_lost += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        if x == 3:
            pc_scissors = "Pc picked: 'Scissors' "
            line1 = Label(root, text=pc_scissors, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            win = "🎊🎊🎊      You win!     🎊🎊🎊"
            line2 = Label(root, text=win, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_won += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played)
            line3.grid(column=1, row=6, padx=20, pady=20)
    elif choice.lower() == 'paper':
        your_emo = '📑'
        if x == 1:
            pc_rock = "Pc picked: 'Rock'"
            line1 = Label(root, text=pc_rock, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            win = "🎊🎊🎊      You win!     🎊🎊🎊"
            line2 = Label(root, text=win, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_won += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 2:
            t_played += 1
            pc_paper = "Pc picked: 'Paper'"
            line1 = Label(root, text=pc_paper, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            tie = "It's a tie!"
            line2 = Label(root, text=tie)
            line2.grid(column=1, row=5, padx=20, pady=20)
            try_ = "Try again"
            line3 = Label(root, text=try_, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 3:
            pc_scissor = "Pc picked: 'Scissors'"
            line1 = Label(root, text=pc_scissor, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            loose = "😞🙁     You loose!      🙁😞"
            line2 = Label(root, text=loose)
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_lost += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
    elif choice.lower() == 'scissors':
        your_emo = '✂️'
        if x == 1:
            pc_rock = "Pc picked: 'Rock'"
            line1 = Label(root, text=pc_rock, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            loose = "😞🙁     You loose!      🙁😞"
            line2 = Label(root, text=loose, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_lost += 1
            t_played += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 2:
            pc_paper = "Pc picked: 'Paper'"
            line1 = Label(root, text=pc_paper, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            win = "🎊🎊🎊      You win!     🎊🎊🎊"
            line2 = Label(root, text=win, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_won += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 3:
            t_played += 1
            pc_scissor = "Pc picked: 'Scissors'"
            line1 = Label(root, text=pc_scissor, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            tie = "It's a tie!"
            line2 = Label(root, text=tie, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            try_ = "Try again"
            line3 = Label(root, text=try_, )
            line3.grid(column=1, row=6, padx=20, pady=20)
    else:
        option = "Did not get that  :(\n\nyour option are:\nRock, paper, scissors"
        line1 = Label(root, text=option)
        line1.grid(column=1, row=4, padx=20, pady=10)
        try_ = "Try again!"
        line2 = Label(root, text=try_, )
        line2.grid(column=1, row=5, padx=20, pady=(20, 5))

    if your_emo != '':
        emos = f"You --->     {your_emo}   vs   {pc_emo}     <--- Pc "
        line0 = Label(root, text=emos)
        line0.grid(column=1, row=3, pady=15)

    try:
        reset_btm.destroy()
    except NameError:
        pass
    if t_played != 0:
        reset_btm = Button(root, text='reset score', command=reset)
        reset_btm.grid(column=1, row=10, padx=10, pady=(2, 10))

def enter(event):
    global line0
    global line1
    global line2
    global line3
    global reset_btm
    global t_played
    global t_won
    global t_lost
    try:
        line0.destroy()
    except NameError:
        pass
    try:
        line1.destroy()
    except NameError:
        pass
    try:
        line2.destroy()
    except NameError:
        pass
    try:
        line3.destroy()
    except NameError:
        pass

    x = random.randint(1, 3)  # 1= rock. 2= paper. 3= scissors

    choice = choise_.get()
    choise_.delete(0, last=30)

    your_emo = ''
    pc_emo = ''
    if x == 1:
        pc_emo = '🪨'
    elif x == 2:
        pc_emo = '📑'
    elif x == 3:
        pc_emo = '✂️'
    else:
        pc_emo = 'Error'

    if choice.lower() == 'rock':
        your_emo = '🪨'
        if x == 1:
            t_played += 1
            pc_rock = "Pc picked: 'Rock' "
            line1 = Label(root, text=pc_rock,)
            line1.grid(column=1, row=4, padx=20, pady=20)
            tie = "It's a tie!"
            line2 = Label(root, text=tie)
            line2.grid(column=1, row=5, padx=20, pady=20)
            try_ = "Try again"
            line3 = Label(root, text=try_, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        if x == 2:
            pc_paper = "Pc picked: 'Paper' "
            line1 = Label(root, text=pc_paper, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            loose = "😞🙁     You loose!      🙁😞"
            line2 = Label(root, text=loose, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_lost += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        if x == 3:
            pc_scissors = "Pc picked: 'Scissors' "
            line1 = Label(root, text=pc_scissors, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            win = "🎊🎊🎊      You win!     🎊🎊🎊"
            line2 = Label(root, text=win, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_won += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played)
            line3.grid(column=1, row=6, padx=20, pady=20)
    elif choice.lower() == 'paper':
        your_emo = '📑'
        if x == 1:
            pc_rock = "Pc picked: 'Rock'"
            line1 = Label(root, text=pc_rock, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            win = "🎊🎊🎊      You win!     🎊🎊🎊"
            line2 = Label(root, text=win, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_won += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 2:
            t_played += 1
            pc_paper = "Pc picked: 'Paper'"
            line1 = Label(root, text=pc_paper, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            tie = "It's a tie!"
            line2 = Label(root, text=tie)
            line2.grid(column=1, row=5, padx=20, pady=20)
            try_ = "Try again"
            line3 = Label(root, text=try_, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 3:
            pc_scissor = "Pc picked: 'Scissors'"
            line1 = Label(root, text=pc_scissor, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            loose = "😞🙁     You loose!      🙁😞"
            line2 = Label(root, text=loose)
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_lost += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
    elif choice.lower() == 'scissors':
        your_emo = '✂️'
        if x == 1:
            pc_rock = "Pc picked: 'Rock'"
            line1 = Label(root, text=pc_rock, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            loose = "😞🙁     You loose!      🙁😞"
            line2 = Label(root, text=loose, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_lost += 1
            t_played += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 2:
            pc_paper = "Pc picked: 'Paper'"
            line1 = Label(root, text=pc_paper, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            win = "🎊🎊🎊      You win!     🎊🎊🎊"
            line2 = Label(root, text=win, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            t_played += 1
            t_won += 1
            played = f"You've played {t_played} times,\nwon {t_won} times and lost {t_lost} times."
            line3 = Label(root, text=played, )
            line3.grid(column=1, row=6, padx=20, pady=20)
        elif x == 3:
            t_played += 1
            pc_scissor = "Pc picked: 'Scissors'"
            line1 = Label(root, text=pc_scissor, )
            line1.grid(column=1, row=4, padx=20, pady=20)
            tie = "It's a tie!"
            line2 = Label(root, text=tie, )
            line2.grid(column=1, row=5, padx=20, pady=20)
            try_ = "Try again"
            line3 = Label(root, text=try_, )
            line3.grid(column=1, row=6, padx=20, pady=20)
    else:
        option = "Did not get that  :(\n\nyour option are:\nRock, paper, scissors"
        line1 = Label(root, text=option)
        line1.grid(column=1, row=4, padx=20, pady=10)
        try_ = "Try again!"
        line2 = Label(root, text=try_, )
        line2.grid(column=1, row=5, padx=20, pady=(20, 5))

    if your_emo != '':
        emos = f"You --->     {your_emo}   vs   {pc_emo}     <--- Pc "
        line0 = Label(root, text=emos)
        line0.grid(column=1, row=3, pady=15)

    try:
        reset_btm.destroy()
    except NameError:
        pass
    if t_played != 0:
        reset_btm = Button(root, text='reset score', command=reset)
        reset_btm.grid(column=1, row=10, padx=10, pady=(2, 10))


welcome = ("""
  ***************************************

**   WELCOME TO ROCK, PAPER, SCISSORS!   **

  ***************************************

Can you beat the computer?
Let's  see!
""")
Label(text=welcome, font='Dairyland').grid(columnspan=3, column=0, row=0, padx=20, pady=20)

choise_ = Entry(root, width=33)
choise_.grid(columnspan=3, row=1, column=0, padx=0, pady=(10, 8))

Button(root, text='play', command=play, width=7).grid(column=1, row=2, padx=10, pady=(2, 10))


root.bind('<Return>', enter)

root.mainloop()

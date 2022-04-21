from tkinter import *
from tkinter import messagebox

player = 1
table = [0, 0, 0, 0, 0, 0, 0, 0, 0]
step = 0

def winner(index, play):
    global step
    global table
    table[index] = play
    step = step + 1
    if table[0] == 1 and table[1] == 1 and table[2] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[3] == 1 and table[4] == 1 and table[5] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[6] == 1 and table[7] == 1 and table[8] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[0] == 1 and table[3] == 1 and table[6] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[1] == 1 and table[4] == 1 and table[7] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[2] == 1 and table[5] == 1 and table[8] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[0] == 1 and table[4] == 1 and table[8] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[2] == 1 and table[4] == 1 and table[6] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    if table[0] == 1 and table[1] == 1 and table[2] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[3] == 1 and table[4] == 1 and table[5] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[6] == 1 and table[7] == 1 and table[8] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[0] == 1 and table[3] == 1 and table[6] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[1] == 1 and table[4] == 1 and table[7] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[2] == 1 and table[5] == 1 and table[8] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[0] == 1 and table[4] == 1 and table[8] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')

    elif table[2] == 1 and table[4] == 1 and table[6] == 1:
        messagebox.showinfo('Перемога', 'Виграли хрестики ')



    elif table[0] == 2 and table[1] == 2 and table[2] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[3] == 2 and table[4] == 2 and table[5] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[6] == 2 and table[7] == 2 and table[8] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[0] == 2 and table[3] == 2 and table[6] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[1] == 2 and table[4] == 2 and table[7] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[2] == 2 and table[5] == 2 and table[8] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[0] == 2 and table[4] == 2 and table[8] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')

    elif table[2] == 2 and table[4] == 2 and table[6] == 2:
        messagebox.showinfo('Перемога', 'Виграли нулики ')
    elif step==9:
        messagebox.showinfo('Перемога', 'Нічия')


def Btn1():
    global player
    if player == 1:
        b1.config(text="X")
        b1['state'] = 'disabled'
        player = 2
        winner(0, 1)
    else:
        b1.config(text="O")
        b1['state'] = 'disabled'
        player = 1
        winner(0, 2)


def Btn2():
    global player
    if player == 1:
        b2.config(text="X")
        b2['state'] = 'disabled'
        player = 2
        winner(1, 1)
    else:
        b2.config(text="O")
        b2['state'] = 'disabled'
        player = 1
        winner(1, 2)


def Btn3():
    global player
    if player == 1:
        b3.config(text="X")
        b3['state'] = 'disabled'
        player = 2
        winner(2, 1)
    else:
        b3.config(text="O")
        b3['state'] = 'disabled'
        player = 1
        winner(2, 2)


def Btn4():
    global player
    if player == 1:
        b4.config(text="X")
        b4['state'] = 'disabled'
        player = 2
        winner(3, 1)
    else:
        b4.config(text="O")
        b4['state'] = 'disabled'
        player = 1
        winner(3, 2)


def Btn5():
    global player
    if player == 1:
        b5.config(text="X")
        b5['state'] = 'disabled'
        player = 2
        winner(4, 1)
    else:
        b5.config(text="O")
        b5['state'] = 'disabled'
        player = 1
        winner(4, 2)


def Btn6():
    global player
    if player == 1:
        b6.config(text="X")
        b6['state'] = 'disabled'
        player = 2
        winner(5, 1)
    else:
        b6.config(text="O")
        b6['state'] = 'disabled'
        player = 1
        winner(5, 2)


def Btn7():
    global player
    if player == 1:
        b7.config(text="X")
        b7['state'] = 'disabled'
        player = 2
        winner(6, 1)
    else:
        b7.config(text="O")
        b7['state'] = 'disabled'
        player = 1
        winner(6, 2)


def Btn8():
    global player
    if player == 1:
        b8.config(text="X")
        b8['state'] = 'disabled'
        player = 2
        winner(7, 1)
    else:
        b8.config(text="O")
        b8['state'] = 'disabled'
        player = 1
        winner(7, 2)


def Btn9():
    global player
    if player == 1:
        b9.config(text="X")
        b9['state'] = 'disabled'
        player = 2
        winner(8, 1)
    else:
        b9.config(text="O")
        b9['state'] = 'disabled'
        player = 1
        winner(8, 2)


win = Tk()
win.title("Хрестики-нулики")
win.config(bg="#123")
win.geometry('600x600')
win.resizable(False, False)

b1 = Button(win, text='-', command=Btn1, width=3, bg='#123', fg='yellow', font=('Arial', 30, 'bold'))
b1.place(x=50, y=50)
b2 = Button(win, text='-', command=Btn2, width=3, bg='#123', fg='yellow', font=('Arial', 30, 'bold'))
b2.place(x=150, y=50)
b3 = Button(win, text='-', command=Btn3, width=3, bg='#123', fg='yellow', font=('Arial', 30, 'bold'))
b3.place(x=250, y=50)

b4 = Button(win, text='-', width=3, bg='#123', fg='yellow', command=Btn4,
            font=('Arial', 30, 'bold'))
b4.place(x=50, y=150)
b5 = Button(win, text='-', width=3, bg='#123', fg='yellow', command=Btn5,
            font=('Arial', 30, 'bold'))
b5.place(x=150, y=150)
b6 = Button(win, text='-', width=3, bg='#123', fg='yellow', command=Btn6,
            font=('Arial', 30, 'bold'))
b6.place(x=250, y=150)

b7 = Button(win, text='-', width=3, bg='#123', fg='yellow', command=Btn7,
            font=('Arial', 30, 'bold'))
b7.place(x=50, y=250)
b8 = Button(win, text='-', width=3, bg='#123', fg='yellow', command=Btn8,
            font=('Arial', 30, 'bold'))
b8.place(x=150, y=250)
b9 = Button(win, text='-', width=3, bg='#123', fg='yellow', command=Btn9,
            font=('Arial', 30, 'bold'))
b9.place(x=250, y=250)

win.mainloop()

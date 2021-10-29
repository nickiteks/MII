from tkinter import *

import numpy as np
from matplotlib import pyplot as plt


def count_function(x, a, b, c, d, isTrapezoid):
    result = []
    if isTrapezoid:
        for i in x:
            if a <= i <= d:
                if a <= i <= b:
                    result.append(1 - (b - i) / (b - a))
                    continue
                if b <= i <= c:
                    result.append(1)
                    continue
                if c <= i <= d:
                    result.append(1 - (i - c) / (d - c))
                    continue
            else:
                result.append(0)
    else:
        for i in x:
            if a <= i <= c:
                if a <= i <= b:
                    result.append(1 - (b - i) / (b - a))
                    continue
                if b <= i <= c:
                    result.append(1 - (i - b) / (c - b))
            else:
                result.append(0)

    return result


def clicked():
    x = np.arange(100)

    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())

    result = count_function(x, a, b, c, d, CheckVar1.get())
    result_2 = count_function(x, int(fn_2_1.get()), int(fn_2_2.get()), int(fn_2_3.get()), int(fn_2_4.get()),
                              CheckVar2.get())
    result_3 = count_function(x, int(fn_3_1.get()), int(fn_3_2.get()), int(fn_3_3.get()), int(fn_3_4.get()),
                              CheckVar3.get())
    result_4 = count_function(x, int(fn_4_1.get()), int(fn_4_2.get()), int(fn_4_3.get()), int(fn_4_4.get()),
                              CheckVar4.get())

    plt.plot(result)
    plt.plot(result_2)
    plt.plot(result_3)
    plt.plot(result_4)

    plt.show()


window = Tk()
window.title("Оценка эффективностиопераций с валютой")
lbl = Label(window, text="Введите данные")
lbl.grid(column=0, row=0)
window.geometry('400x250')

# function 1
lbl_fn1 = Label(window, text="Функция 1:")
lbl_fn1.grid(column=0, row=1)

fn_1_1 = Entry(window, width=5)
fn_1_1.grid(column=1, row=1)

fn_1_2 = Entry(window, width=5)
fn_1_2.grid(column=2, row=1)

fn_1_3 = Entry(window, width=5)
fn_1_3.grid(column=3, row=1)

fn_1_4 = Entry(window, width=5)
fn_1_4.grid(column=4, row=1)

CheckVar1 = BooleanVar()
chk_fn1 = Checkbutton(window, text='Трапецевидная?', variable=CheckVar1)
chk_fn1.grid(column=5, row=1)

# function 2
lbl_fn2 = Label(window, text="Функция 2:")
lbl_fn2.grid(column=0, row=2)

fn_2_1 = Entry(window, width=5)
fn_2_1.grid(column=1, row=2)

fn_2_2 = Entry(window, width=5)
fn_2_2.grid(column=2, row=2)

fn_2_3 = Entry(window, width=5)
fn_2_3.grid(column=3, row=2)

fn_2_4 = Entry(window, width=5)
fn_2_4.grid(column=4, row=2)

CheckVar2 = BooleanVar()
chk_fn2 = Checkbutton(window, text='Трапецевидная?', variable=CheckVar2)
chk_fn2.grid(column=5, row=2)

# function 3
lbl_fn3 = Label(window, text="Функция 3:")
lbl_fn3.grid(column=0, row=3)

fn_3_1 = Entry(window, width=5)
fn_3_1.grid(column=1, row=3)

fn_3_2 = Entry(window, width=5)
fn_3_2.grid(column=2, row=3)

fn_3_3 = Entry(window, width=5)
fn_3_3.grid(column=3, row=3)

fn_3_4 = Entry(window, width=5)
fn_3_4.grid(column=4, row=3)

CheckVar3 = BooleanVar()
chk_fn3 = Checkbutton(window, text='Трапецевидная?', variable=CheckVar3)
chk_fn3.grid(column=5, row=3)

# function 4
lbl_fn4 = Label(window, text="Функция 4:")
lbl_fn4.grid(column=0, row=4)

fn_4_1 = Entry(window, width=5)
fn_4_1.grid(column=1, row=4)

fn_4_2 = Entry(window, width=5)
fn_4_2.grid(column=2, row=4)

fn_4_3 = Entry(window, width=5)
fn_4_3.grid(column=3, row=4)

fn_4_4 = Entry(window, width=5)
fn_4_4.grid(column=4, row=4)

CheckVar4 = BooleanVar()
chk_fn4 = Checkbutton(window, text='Трапецевидная?', variable=CheckVar4)
chk_fn4.grid(column=5, row=4)

btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=5)

window.mainloop()

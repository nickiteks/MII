import tkinter
import random
from tkinter import *
import pandas as pd

import numpy as np
from matplotlib import pyplot as plt

list_functions = []
clear_time_series = [random.randint(2, 24) for _ in range(50)]
list_time_marks = []
graph_indexes = []
list_tendentions = []
prognoze_list = []


def getNext(listing):
    add_list = []
    predict = listing[len(listing) - 1][1]
    for item in listing:
        if item[0] == predict:
            add_list.append(item)
    a = pd.Index(add_list)
    print(a.value_counts())
    print(a.value_counts().index[0])
    return a.value_counts().index[0][1]


def predict():
    prognoze_list.clear()
    for i in range(len(list_tendentions) - 2):
        list_work = [list_tendentions[i], list_tendentions[i + 1]]
        prognoze_list.append(list_work)
    print(prognoze_list)
    print(getNext(prognoze_list))
    # Определяем лингвистическую метку будующего числа
    graph_indexes.append(graph_indexes[len(graph_indexes) - 1] + getNext(prognoze_list))
    # Находим максимальное опдходящее по лингвистической метке
    max = list_functions[graph_indexes[len(graph_indexes) - 1]][0]

    index = 0
    # Берем нечеткое множество последнее в нашей метке идем по нему и находим максимальное подходящее число
    for i in range(len(list_functions[graph_indexes[len(graph_indexes) - 1]])):
        if list_functions[graph_indexes[len(graph_indexes) - 1]][i] > max:
            max = list_functions[graph_indexes[len(graph_indexes) - 1]][i]
            index = i

    clear_time_series.append(index)
    razn = (clear_time_series[len(clear_time_series) - 2] - clear_time_series[len(clear_time_series) - 1]) / \
           clear_time_series[len(clear_time_series) - 2]

    print(razn)


def graph_tend():
    fig, ax = plt.subplots()
    for x in range(len(list_tendentions) - 1):
        if list_tendentions[x] == list_tendentions[x + 1]:
            plt.plot([x, x + 1], [list_tendentions[x], list_tendentions[x + 1]], color='g')
        if list_tendentions[x + 1] == 0:
            plt.plot([x, x + 1], [list_tendentions[x], list_tendentions[x + 1]], color='g')
        if list_tendentions[x + 1] == 1:
            plt.plot([x, x + 1], [list_tendentions[x], list_tendentions[x + 1]], color='r')
        if list_tendentions[x + 1] == -1:
            plt.plot([x, x + 1], [list_tendentions[x], list_tendentions[x + 1]], color='b')

    plt.show()


def get_tendentions():
    list_tendentions.clear()
    for i in range(len(graph_indexes) - 1):
        if graph_indexes[i] == graph_indexes[i + 1]:
            list_tendentions.append(0)
        if graph_indexes[i] < graph_indexes[i + 1]:
            list_tendentions.append(1)
        if graph_indexes[i] > graph_indexes[i + 1]:
            list_tendentions.append(-1)
    print(list_tendentions)


def graph_NVK():
    plt.plot(list_time_marks)
    plt.show()


def graph_ChVK():
    list_help = clear_time_series.copy()
    a = list_help.pop()
    plt.plot(list_help, color='r')
    list_help.pop()
    list_help.append(a)
    plt.plot(list_help, color='g')
    plt.show()


def print_CTS():
    print(f"---Нечеткий временной ряд---")
    for i in range(len(clear_time_series)):
        print(f"{i}. {list_time_marks[i]} - {clear_time_series[i]}")


# метод нахожения совпадений из нечеткого множества и определение к какому множеству относиться переданное число
def get_max(number):
    list_coinsidens = []
    for i in list_functions:
        list_coinsidens.append(i[number])
    max = list_coinsidens[0]
    index = 0
    for i in range(len(list_coinsidens)):
        if list_coinsidens[i] > max:
            max = list_coinsidens[i]
            index = i
    return index


def get_fuzzy_estimate():
    list_time_marks.clear()
    graph_indexes.clear()
    for i in clear_time_series:
        number = get_max(i)
        graph_indexes.append(number)
        if number <= 2:
            if number == 0:
                list_time_marks.append("холодно")
            if number == 1:
                list_time_marks.append("тепло")
            if number == 2:
                list_time_marks.append("жарко")
        else:
            list_time_marks.append("очень жарко")
    print_CTS()


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

    list_functions.append(count_function(x, a, b, c, d, CheckVar1.get()))
    listbox_update()


def show():
    for i in list_functions:
        plt.plot(i)
    plt.show()


def change():
    list_functions.pop(lbox.curselection()[0])

    x = np.arange(100)

    a = int(fn_1_1.get())
    b = int(fn_1_2.get())
    c = int(fn_1_3.get())
    d = int(fn_1_4.get())

    list_functions.append(count_function(x, a, b, c, d, CheckVar1.get()))
    listbox_update()


def del_function():
    list_functions.pop(lbox.curselection()[0])
    listbox_update()


def dop():
    result = []
    for i in range(len(list_functions[lbox.curselection()[0]])):
        result.append(1 - list_functions[lbox.curselection()[0]][i])
    list_functions.append(result)
    listbox_update()


def listbox_update():
    lbox.delete(0, tkinter.END)
    for i in range(len(list_functions)):
        lbox.insert(i, str(i))


def global_method():
    get_fuzzy_estimate()
    get_tendentions()
    show()
    graph_NVK()
    graph_tend()


window = Tk()
window.title("Оценка эффективностиопераций с валютой")
lbl = Label(window, text="Введите данные")
lbl.grid(column=0, row=0)
window.geometry('750x400')

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

btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=5)

btn_del = Button(window, text="Показать!", command=show)
btn_del.grid(column=5, row=5)

btn_change = Button(window, text="Изменить!", command=change)
btn_change.grid(column=2, row=6)

btn_del = Button(window, text="Удалить!", command=del_function)
btn_del.grid(column=3, row=6)

btn_del = Button(window, text="Дополнить!", command=dop)
btn_del.grid(column=3, row=7)

lbox = Listbox(width=15, height=8)
lbox.grid(column=1, row=8)

btn_time = Button(window, text="НВР!", command=get_fuzzy_estimate)
btn_time.grid(column=8, row=10)

btn_tend = Button(window, text="Тенденции!", command=get_tendentions)
btn_tend.grid(column=9, row=10)

btn_graph_ChVK = Button(window, text="График предсказания", command=graph_ChVK)
btn_graph_ChVK.grid(column=7, row=11)

btn_graph_NVK = Button(window, text="График НВР!", command=graph_NVK)
btn_graph_NVK.grid(column=8, row=11)

btn_graph_tend = Button(window, text="График тенденций!", command=graph_tend)
btn_graph_tend.grid(column=9, row=11)

btn_global = Button(window, text="Глобальный клик", command=global_method)
btn_global.grid(column=8, row=9)

btn_pred = Button(window, text="Прогноз!", command=predict)
btn_pred.grid(column=7, row=7)

x = np.arange(100)
list_functions.append(count_function(x, 1, 10, 14, 100, True))
list_functions.append(count_function(x, 1, 15, 20, 100, True))
list_functions.append(count_function(x, 1, 21, 30, 100, True))
listbox_update()

window.mainloop()

from tkinter import *
import pandas as pd

k = 0
route = []
mas = []

def btn_click():
    global k
    global lbl
    global dr
    global mas
    if k < 8:
        txt = ent.get()
        txt = txt.split(',')
        route.append(txt)
        route.sort(key = lambda way: way[2])
    k += 1
    if k == 8:
        btn.config(text = 'Конвертировать в CSV', command = btn_click)
        lbl.config(text = "Введите название файла")
    if k == 9:
        txt = ent.get()
        dr = pd.DataFrame(route, columns=['Начало', 'Конец', 'Номер'])
        dr.to_csv(txt, sep=',', index = False)
        mas = dr.to_records(index = False)
        btn.config(text = 'Вывести строку')
    if k == 10:
        txt = 0
        for i in range(8):
            if mas[i][-1] == ent.get():
                txt = 'Начало: ' + mas[i][0] + '\n' + 'Конец: ' + mas[i][1] + '\n' + 'Номер: ' + mas[i][-1]
                lbl.config(text = txt)
                break
        if txt == 0:
            lbl.config(text = 'Такого маршрута нет!')

root = Tk()
root.title('Route')
root.geometry('400x300')

ent = Entry(root)
ent.pack(side = TOP)

btn = Button(root)
btn.config(text = 'Добавить строку', command = btn_click)
btn.pack(side = TOP)

lbl = Label(root, text = 'Тут будет таблица')
lbl.pack(side = TOP)

root.mainloop()

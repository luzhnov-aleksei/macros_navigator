import pyautogui as pg
from time import sleep
from tkinter import*
import keyboard

#sleep(5)
#print(pg.position())
root = Tk()
root.title("Макрос")
root.resizable(False, False)
root.geometry('300x240+750+300')




def macros():
    dur = 0.1 # задержка
    x,y = 442, 292 # начальные координаты

    lines = int(ent_lines.get())
    columns = int(ent_columns.get())
    #root.destroy()
    sleep(3)

    for _ in range(columns):
        for _ in range(lines):
            pg.click(x, y) # начальная точка (левый верхний угол)
            pg.move(10, 10, duration = dur)
            pg.click()
            sleep(dur)
            y +=34
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('Скрипт остановлен')
                exit() 

        y = 292
        x += 50



lbl_1 = Label(font = 'Arial 10', text = '''\n СКРИПТ ДЛЯ ОТМЕТКИ ПОСЕЩАЕМОСТИ
 В НАВИГАТОРЕ\n 
1) Установите масштаб страницы 100%
2) Пролистайте страницу максимально вверх
3) Введите  кол-во строк''')
ent_lines = Entry(font = 'Arial 10', justify=CENTER, width= 5)
lbl_2 = Label(font = 'Arial 10', text = "4) Введите кол-во столбцов")
ent_columns = Entry(font = 'Arial 10', justify=CENTER, width= 5)
btn = Button(font = 'Arial 13', text = "ЗАПУСК", command= macros)
lbl_empty = Label()

lbl_1.pack()
ent_lines.pack()
lbl_2.pack()
ent_columns.pack()
lbl_empty.pack()
btn.pack()


root.mainloop()
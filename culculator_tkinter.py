import tkinter

#создаем основное окно, даем ему имя и размер
window = tkinter.Tk()
window.title("Мой калькулятор")
window.geometry("300x300")
window.configure(bg = "silver")

def get_num1():
    num1 = int(text_num1.get())
    return num1
def get_num2():
    num2 = int(text_num2.get())
    return num2
def set_answer(answer):
    text_answer.delete(0, "end")
    text_answer.insert(0, answer)

#функция для сложения чисел
def add():
    print("Выполним сложение")
    #вызываем функцию, которая преобразует строку в число
    num1 = get_num1()
    num2 = get_num2()
    #складываем
    result = num1 + num2
    #передаем в фунцию set_result рещультат действия
    set_answer(result)

#функция для вычитания чисел
def sub():
    print("Выполним вычитание")
    #передаем в фунцию значения из текстового окна
    num1 = get_num1()
    num2 = get_num2()
    result = num1 - num2
    set_answer(result)

def mul():
    print("Выполним умножение")
    num1 = get_num1()
    num2 = get_num2()
    result = num1 * num2
    set_answer(result)

def div():
    print("Выполним деление")
    num1 = get_num1()
    num2 = get_num2()
    result = num1 / num2
    set_answer(result)

#оздаем кнопку, которая отвечает за сложение чисел, присваиваем то, что будет на кнопке и вызываем функцию 
button_add = tkinter.Button(window, text = "+", command = add, width = 7, height = 1, bg = "gold")
#задаем расположение кнопки
button_add.place(x = 95, y = 110)

#кнопка, которая отвечает за вычитаение
button_sub = tkinter.Button(window, text = "-", command = sub, width = 7, height = 1, bg = "gold")
button_sub.place(x = 160, y = 110)

#кнопка, которая отвечает за умножение чисел
button_mul = tkinter.Button(window, text = "*", command = mul, width = 7, height = 1, bg = "gold")
button_mul.place(x = 95, y = 140)

#кнопка, которая отвечает за деление чисел
button_div = tkinter.Button(window, text = "/", command = div, width = 7, height = 1, bg = "gold")
button_div.place(x = 160, y = 140)

#текстовое поле для 1 числа
text_num1 = tkinter.Entry(window, width = 20, bg = "black", fg = "gold")
text_num1.place(x = 95, y = 40)

#текстовое поле для 2 числа
text_num2 = tkinter.Entry(window, width = 20, bg = "black", fg = "gold")
text_num2.place(x = 95, y = 81)

#текстовое поле для вывода ответа
text_answer = tkinter.Entry(window, width = 20, bg = "black", fg = "gold")
text_answer.place(x = 95, y = 221)

#добавляем надпись 
label_num1 = tkinter.Label(window, text = "Введите первое число", background = "silver")
label_num1.place(x = 95, y = 20)

label_num2 = tkinter.Label(window, text = "Введите второе число", background = "silver")
label_num2.place(x = 95, y = 61)

label_answer = tkinter.Label(window, text = "Ответ", background = "silver")
label_answer.place(x = 95, y = 200)

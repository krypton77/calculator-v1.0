import tkinter as tk
from tkinter import ttk
from tkinter import *
import math, time

app = tk.Tk()
app.title('Calculator v1.0')
text_field = ttk.Entry(app, width=25, font='verdana 20')
text_field.grid(row=1, column=1)
length = 0
result = 0

commands = {
    'divide': '/',
    'multiply': '*',
    'sum': '+',
    'difference': '-',
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
    '00': '00',
    '.': '.',
    }

def index():
    text = text_field.get()
    #print(type(text))
    length = len(text)

def clearing():
	text_field.delete(0, END)

def action(btn):
    index()
    text_field.insert(50-length, commands.get(btn))

def dividing():
    action('divide')

def multiplying():
    action('multiply')

def summing():
    action('sum')

def differing():
    action('difference')

def number_1():
    action('1')

def number_2():
    action('2')

def number_3():
    action('3')

def number_4():
    action('4')

def number_5():
    action('5')

def number_6():
    action('6')

def number_7():
    action('7')

def number_8():
    action('8')

def number_9():
    action('9')

def number_0():
    action('0')

def number_00():
    action('00')

def dot():
    action('.')

def solution(self):
    result = text_field.get()
    length = len(result)
    try:
        result = eval(result)
    except NameError:
        clearing()
        text_field.insert(0, 'Do not use latters!')
        app.after(2000, clearing)
    result = round(result, length)
    temp = math.modf(result)
    if temp[0] == 0:
        result = int(result)
    clearing()
    return text_field.insert(0, result)

def solve():
    solution(0)

######################################

btn_clear = tk.Button(app, text='C', width=10, height=2, font='verdana 14 bold', command=clearing)
btn_clear.grid(row=1, column=2)
btn_clear.config(bg='#F4E2BF')

btn_sum = tk.Button(app, text='=', width=10, height=2, font='verdana 14 bold', command=solve)
btn_sum.grid(row=2, column=2)
btn_sum.config(bg='#b3ffff')

btn_multiply = tk.Button(app, text='*', width=10, height=2, font='verdana 14 bold', command=multiplying)
btn_multiply.grid(row=3, column=2)

btn_sum = tk.Button(app, text='+', width=10, height=2, font='verdana 14 bold', command=summing)
btn_sum.grid(row=4, column=2)

btn_difference = tk.Button(app, text='-', width=10, height=2, font='verdana 14 bold', command=differing)
btn_difference.grid(row=5, column=2)

########################################

btn_one = tk.Button(app, text='1', width=10, height=2, font='verdana 14 bold', command=number_1)
btn_one.grid(row=2, column=1, sticky=W)

btn_two = tk.Button(app, text='2', width=10, height=2, font='verdana 14 bold', command=number_2)
btn_two.grid(row=2, column=1)

btn_three = tk.Button(app, text='3', width=10, height=2, font='verdana 14 bold', command=number_3)
btn_three.grid(row=2, column=1, sticky=E)

########################################

btn_four = tk.Button(app, text='4', width=10, height=2, font='verdana 14 bold', command=number_4)
btn_four.grid(row=3, column=1, sticky=W)

btn_five = tk.Button(app, text='5', width=10, height=2, font='verdana 14 bold', command=number_5)
btn_five.grid(row=3, column=1)

btn_six = tk.Button(app, text='6', width=10, height=2, font='verdana 14 bold', command=number_6)
btn_six.grid(row=3, column=1, sticky=E)

########################################

btn_seven = tk.Button(app, text='7', width=10, height=2, font='verdana 14 bold', command=number_7)
btn_seven.grid(row=4, column=1, sticky=W)

btn_eight = tk.Button(app, text='8', width=10, height=2, font='verdana 14 bold', command=number_8)
btn_eight.grid(row=4, column=1)

btn_nine = tk.Button(app, text='9', width=10, height=2, font='verdana 14 bold', command=number_9)
btn_nine.grid(row=4, column=1, sticky=E)

########################################

btn_zero = tk.Button(app, text='0', width=10, height=2, font='verdana 14 bold', command=number_0)
btn_zero.grid(row=5, column=1, sticky=W)

btn_dot = tk.Button(app, text='.', width=10, height=2, font='verdana 14 bold', command=dot)
btn_dot.grid(row=5, column=1)

btn_divide = tk.Button(app, text='/', width=10, height=2, font='verdana 14 bold', command=dividing)
btn_divide.grid(row=5, column=1, sticky=E)

text_field.bind('<Return>', solution)
text_field.focus() # сразу активное текстовое поле
app.resizable(False, False)

app.mainloop()

from tkinter import *

root = Tk()
root.title('calculator')

screen = Entry(root, width=35, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# functions of the buttons

def button_click(number):
     current = screen.get()
     screen.delete(0, END)
     screen.insert(0, str(current) + str(number))


def button_clear():
     screen.delete(0, END)

def button_add():
     a_num = screen.get()
     global first_number
     global math
     math='add'
     first_number = int(a_num)
     screen.delete(0, END)
     
def button_minus():
     m_num = screen.get()
     global first_number
     global math
     math='subtract'
     first_number = int(m_num)
     screen.delete(0, END)

def button_multi():
     multi_num = screen.get()
     global first_number
     global math
     math='multiply'
     first_number = int(multi_num)
     screen.delete(0, END)

def button_div():
     d_num = screen.get()
     global first_number
     global math
     math='divide'
     first_number = int(d_num)
     screen.delete(0, END)
     
def button_equal():
     second_number = screen.get()
     screen.delete(0, END)
     if math =='add':
       screen.insert(0, first_number + int(second_number))
     if math =='subtract':
       screen.insert(0, first_number - int(second_number))
     if math =='multiply':
       screen.insert(0, first_number * int(second_number))
     if math =='divide':
       screen.insert(0, first_number / int(second_number))
# define buttons

button_1 = Button(root, text='1', padx=40, pady=40, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=40, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=40, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=40, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=40, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=40, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=40, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=40, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=40, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=40, pady=20, command= button_add)
button_minus = Button(root, text='-', padx=40, pady=40, command= button_minus)
button_multi = Button(root, text='*', padx=40, pady=40, command= button_multi)
button_div = Button(root, text='/', padx=40, pady=40, command= button_div)
button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=80, pady=20, command = button_clear)
# buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_minus.grid(row=1, column=3)
button_multi.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()

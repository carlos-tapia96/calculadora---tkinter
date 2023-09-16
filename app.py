from tkinter import *

root = Tk()
root.title("Calculadora")

font_size = 24
font =('Helvetica', font_size)

root.geometry("400x300")
root.resizable(False,False)

display=Entry(root, font=font)
display.grid(row=1,columnspan=8,sticky=W+E, padx=10, pady=10)

root.configure(bg="lightgray")
button_style = {'padx': 20, 'pady': 10, 'bg': 'lightgray', 'font': ('Helvetica', 10)}

for i in range(4):
    root.columnconfigure(i, weight=1)
i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1

def get_operation(operator):
    global i
    operator_length=len(operator)
    display.insert(i, operator)
    i+=operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0,display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')

def calculate():
    display_state = display.get()
    try:
        math_expression = compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, 'Error')

# NUMERIC BOTONES
Button(root,text="1", command=lambda:get_numbers(1), **button_style).grid(row=2, column=0,sticky=W+E)
Button(root,text="2", command=lambda:get_numbers(2), **button_style).grid(row=2, column=1,sticky=W+E)
Button(root,text="3", command=lambda:get_numbers(3), **button_style).grid(row=2, column=2,sticky=W+E)

Button(root,text="4", command=lambda:get_numbers(4), **button_style).grid(row=3, column=0,sticky=W+E)
Button(root,text="5", command=lambda:get_numbers(5), **button_style).grid(row=3, column=1,sticky=W+E)
Button(root,text="6", command=lambda:get_numbers(6), **button_style).grid(row=3, column=2,sticky=W+E)

Button(root,text="7", command=lambda:get_numbers(7), **button_style).grid(row=4, column=0,sticky=W+E)
Button(root,text="8", command=lambda:get_numbers(8), **button_style).grid(row=4, column=1,sticky=W+E)
Button(root,text="9", command=lambda:get_numbers(9), **button_style).grid(row=4, column=2,sticky=W+E)

# BOTONES PARTE 2

Button(root,text="AC", command=lambda:clear_display(), **button_style).grid(row=5, column=0,sticky=W+E)
Button(root,text="0", command=lambda:get_numbers(0), **button_style).grid(row=5, column=1,sticky=W+E)
Button(root,text="%", command=lambda: get_operation("%"), **button_style).grid(row=5, column=2,sticky=W+E)

Button(root,text="+", command=lambda: get_operation("+"), **button_style).grid(row=2, column=3,sticky=W+E)
Button(root,text="-", command=lambda: get_operation("-"), **button_style).grid(row=3, column=3,sticky=W+E)
Button(root,text="*", command=lambda: get_operation("*"), **button_style).grid(row=4, column=3,sticky=W+E)
Button(root,text="/", command=lambda: get_operation("/"), **button_style).grid(row=5, column=3,sticky=W+E)

Button(root,text="←", command=lambda:undo(), **button_style).grid(row=2, column=4,sticky=W+E,columnspan =2)
Button(root,text="exp", command=lambda: get_operation("**"), **button_style).grid(row=3, column=4,sticky=W+E)
Button(root,text="^2", command=lambda: get_operation("**2"), **button_style).grid(row=3, column=5,sticky=W+E)
Button(root,text="(", command=lambda: get_operation("("), **button_style).grid(row=4, column=4,sticky=W+E)
Button(root,text=")", command=lambda: get_operation(")"), **button_style).grid(row=4, column=5,sticky=W+E)
Button(root,text="=", command = lambda:calculate(), **button_style).grid(row=5, column=4,sticky=W+E, columnspan =2)



root.mainloop()

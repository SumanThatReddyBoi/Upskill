from tkinter import *
expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg = "white")
    root.title("Basic Graphical Calculator")
    #root.geometry("300x150")
    display = StringVar()
    entry = Entry(root,textvariable = display)
    entry.grid(columnspan = 4, ipadx = 70)

    #Numbers
    btn1 = Button(root, text='1', fg='black', bg='orange', command=lambda: press(1), height=1, width=10)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='orange', command=lambda: press(2), height=1, width=10)
    btn2.grid(row=2, column=1)   
    btn3 = Button(root, text='3', fg='black', bg='orange', command=lambda: press(3), height=1, width=10)
    btn3.grid(row=2, column=2)   
    btn4 = Button(root, text='4', fg='black', bg='orange', command=lambda: press(4), height=1, width=10)
    btn4.grid(row=3, column=0)   
    btn5 = Button(root, text='5', fg='black', bg='orange', command=lambda: press(5), height=1, width=10)
    btn5.grid(row=3, column=1)   
    btn6 = Button(root, text='6', fg='black', bg='orange', command=lambda: press(6), height=1, width=10)
    btn6.grid(row=3, column=2)   
    btn7 = Button(root, text='7', fg='black', bg='orange', command=lambda: press(7), height=1, width=10)
    btn7.grid(row=4, column=0)   
    btn8 = Button(root, text='8', fg='black', bg='orange', command=lambda: press(8), height=1, width=10)
    btn8.grid(row=4, column=1)   
    btn9 = Button(root, text='9', fg='black', bg='orange', command=lambda: press(9), height=1, width=10)
    btn9.grid(row=4, column=2)   
    btn0 = Button(root, text='0', fg='black', bg='orange', command=lambda: press(0), height=1, width=10)
    btn0.grid(row=5, column=0)       

    #Operators
    plus = Button(root, text='+', fg='black', bg='orange', command=lambda: press('+'), height=1, width=10)
    plus.grid(row=2, column=3)   
    minus = Button(root, text='-', fg='black', bg='orange', command=lambda: press('-'), height=1, width=10)
    minus.grid(row=3, column=3)   
    mul = Button(root, text='*', fg='black', bg='orange', command=lambda: press('*'), height=1, width=10)
    mul.grid(row=4, column=3)   
    div = Button(root, text='/', fg='black', bg='orange', command=lambda: press('/'), height=1, width=10)
    div.grid(row=5, column=3)   

    #Extra
    eq = Button(root, text='=', fg='black', bg='orange', command=equal, height=1, width=10)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='black', bg='orange', command=clear, height=1, width=10)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='black', bg='orange', command=lambda: press('.'), height=1, width=10)
    dot.grid(row=6, column=0)

    root.mainloop()
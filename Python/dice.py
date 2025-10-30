import tkinter as tk
import random

root = tk.Tk()
root.geometry('650x650')
root.title('Roll Two Dice')

label = tk.Label(root, text='', font=('Times New Roman', 400))

def roll():
    die=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    print(f'{random.choice(die)} {random.choice(die)}')
    label.configure(text=f'{random.choice(die)} {random.choice(die)}')
    label.pack()

button = tk.Button(root, text='Roll Dice', foreground='black', command=roll, width=50, height=2)

button.pack()

root.mainloop()
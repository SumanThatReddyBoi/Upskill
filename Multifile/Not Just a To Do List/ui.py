import tkinter as tk
from tkinter import simpledialog, messagebox
import todo
from notifier import alerter

class GenderDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Select your gender:").pack(anchor="w")

        self.gender_var = tk.StringVar(value="RATHER NOT SAY")
        
        options = [
            ("Male", "MALE"),
            ("Female", "FEMALE"),
            ("Rather Not Say", "RATHER NOT SAY")]



        for label, value in options:
            tk.Radiobutton(master, text=label, value=value, variable=self.gender_var).pack(anchor="w")
        return None

    def apply(self):
        self.result = self.gender_var.get()


def ask_user_info():
    todo.email = simpledialog.askstring("Email", "Enter your email:")
    if not todo.email:
        messagebox.showerror("Error", "Email cannot be empty!")
        return False
    if not todo.email_validity(todo.email):
        messagebox.showerror("Error", "Invalid email address!")
        return False

    dialog = GenderDialog(root, title="Gender Selection")
    gender = dialog.result

    if not gender:
        messagebox.showerror("Error", "Gender not selected!")
        return False
    if gender == "MALE":
        name = simpledialog.askstring("Name", "Enter your preferred name:")
        todo.username = f"Mr. {name}"
    elif gender == "FEMALE":
        name = simpledialog.askstring("Name", "Enter your preferred name:")
        todo.username = f"Ms. {name}"
    else:
        todo.username = "Anonymous"
    messagebox.showinfo("Saved", "Email settings saved successfully!")
    return True


def update_listbox():
    task_list.delete(0, tk.END)
    if not todo.todo:
        task_list.insert(tk.END, "Your list is empty.")
        return
    for i, item in enumerate(todo.todo):
        status = "✓" if item["Status"] else "✗"
        task_list.insert(tk.END, f"{i+1}. [{status}] {item['Task']} - {item['Description']}")


def add_task():
    task = task_entry.get().strip()
    desc = desc_entry.get().strip()

    if not task or not desc:
        messagebox.showerror("Error", "Task and/or description cannot be empty!")
        return

    todo.add(task, desc)
    task_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    update_listbox()

    task_entry.focus_set()


def delete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to delete.")
        return
    todo.remove(selected[0])
    update_listbox()


def mark_complete():
    selected = task_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to mark complete.")
        return

    todo.done(selected[0])
    update_listbox()


def mark_incomplete():
    selected = task_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to mark incomplete.")
        return

    todo.not_done(selected[0])
    update_listbox()


def email_list():
    if todo.email in (None, "NULL"):
        if not ask_user_info():
            return

    mail_body = todo.view(return_text=True)

    mail_content = f"""
Hello {todo.username},

This is a message from Not Just A To Do List. 

As per your request, we are sending you your to-do list. 
This email and any further emails will only be sent upon request.

{mail_body}

Thank you for choosing Not Just A To Do List!
"""

    try:
        alerter(todo.email, mail_content)
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))




root = tk.Tk()
root.title("Not Just A ToDo List")
root.geometry("590x520")

title = tk.Label(root, text="Not Just A To Do List", font=("Arial", 20, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Task:").grid(row=0, column=0)
task_entry = tk.Entry(frame, width=30)
task_entry.grid(row=0, column=1)

tk.Label(frame, text="Description:").grid(row=1, column=0)
desc_entry = tk.Entry(frame, width=30)
desc_entry.grid(row=1, column=1)
desc_entry.bind("<Return>", lambda event: add_task())

task_list = tk.Listbox(root, width=60, height=15)
task_list.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10, fill="x")

for i in range(3):
    btn_frame.grid_columnconfigure(i, weight=1)


tk.Button(btn_frame, text="Mark Complete", command=mark_complete)\
    .grid(row=0, column=0, padx=8, pady=6, sticky="ew")

tk.Button(btn_frame, text="Mark Incomplete", command=mark_incomplete)\
    .grid(row=0, column=1, padx=8, pady=6, sticky="ew")

tk.Button(btn_frame, text="Email My List", command=email_list)\
    .grid(row=0, column=2, padx=8, pady=6, sticky="ew")

tk.Button(btn_frame, text="Add Task", command=add_task)\
    .grid(row=1, column=0, padx=8, pady=6, sticky="ew")

tk.Button(btn_frame, text="Delete", command=delete_task)\
    .grid(row=1, column=1, padx=8, pady=6, sticky="ew")

tk.Button(btn_frame, text="Exit", command=root.quit)\
    .grid(row=1, column=2, padx=8, pady=6, sticky="ew")


update_listbox()
root.mainloop()

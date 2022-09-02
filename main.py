from tkinter import *
from tkinter import messagebox
import webbrowser

window = Tk()

def yes():
    for i in range(0,10):
        webbrowser.open_new_tab("website of your chossing")

def devol():
    if name.get() == "" and password.get() == "":
        messagebox.showinfo("Please input name and password", "Please input name and password")
        return
    root = Tk()
    l1 = Label(root, font=("Arial", 30), text="You may regret this(this is not a  rick roll)")
    l1.pack()
    exit_button = Button(root, font=("Arial", 20), text="Yes", command=yes)
    exit_button.pack(pady=20)


def submit():
    if name.get() == "" and password.get() == "":
        messagebox.showinfo("Please input name and password")
        return
    name.config(state='disable')
    password.config(state='disable')


name = Entry(window, font=("Arial", 30))
name.pack(side=LEFT)

password = Entry(window, font=("Arial", 30), show="*")
password.pack(side=LEFT)

submit = Button(window, font=("Arial", 20), command=submit, text="Submit")
submit.pack()

button = Button(window, font=("Arial", 20), text="Click me for free vbucks", command=devol)
button.pack()

window.title("Free vbucks")
window.resizable(False, False)
window.mainloop()

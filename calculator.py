from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()  

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.configure(background='grey')
root.geometry("350x580")
root.title("Calculator")


Label(root, text="Calculator", font="Helvetica 20 bold", fg='purple').pack(pady=5)
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 20 bold")
screen.pack(fill='x', padx=10, pady=10, ipady=5)

# frame 5
frame1 = Frame(root, bg='grey')
b = Button(frame1, text="C", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=4, pady=10)

b = Button(frame1, text="()", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="%", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="/", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)
frame1.pack()


frame1 = Frame(root, bg='grey')
b = Button(frame1, text="7", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="8", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="9", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="*", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)
frame1.pack()

# frame 2
frame1 = Frame(root, bg='grey', width="320")
b = Button(frame1, text="4", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="5", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="6", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="-", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)
frame1.pack()

# frame 3
frame1 = Frame(root, bg='grey')
b = Button(frame1, text="1", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="2", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="3", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="+", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)
frame1.pack()

# frame 4
frame1 = Frame(root, bg='grey')
b = Button(frame1, text="+/-", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=4, pady=10)

b = Button(frame1, text="0", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text=".", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)

b = Button(frame1, text="=", font="lucida 20 bold", borderwidth=5, padx=5, pady=5)
b.bind("<Button-1>", click)
b.pack(side=LEFT, anchor='nw', padx=10, pady=10)
frame1.pack()

root.mainloop()
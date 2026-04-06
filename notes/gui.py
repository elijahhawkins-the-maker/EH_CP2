import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.minsize(250,250)
root.maxsize(1500,1500)
root.geometry("300x300+100+100")
start = tk.Label(root, text="This is my first GUI", font = ("Times New Roman", 30, "bold"))
start.config(fg = "purple", background = 'green')
start.pack()
tk.Label(root, text="This is a label").pack()

root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count)

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)

def mult():
    root.count *= 500
    lbl['text'] = str(root.count)
def div():
    root.count /= 5
    lbl["text"] = str(root.count)

btn = tk.Button(root, text="ADD", command=add)
btn.pack()
btn2 = tk.Button(root, text="SUB", command = sub)
btn2.pack()
btn3 = tk.Button(root, text="multiply", command= mult)
btn3.pack()
btn4 = tk.Button(root, text = "divide", command = div)
btn4.pack()
lbl = tk.Label(root, text = "0")
lbl.pack()

root.mainloop()
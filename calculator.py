from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("240x400")

entry = Entry(root, width=20, font=("Arial", 20), bd=10, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4,  padx=10, ipadx=5, ipady=10)

def press(ch):
    entry.insert(END, ch)

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")
        
def delete():
    text = entry.get()
    if text:
        entry.delete(len(text) - 1, END)
        
buttons = [
    "AC","%","del","/",
    "7","8","9","*",
    "4","5","6","-",
    "1","2","3","+",
    "00","0",".","="
]

row = 1
col = 0

for b in buttons:
    if b == "AC":
        cmd = clear
    else:
        cmd = lambda x=b: press(x)
    Button(root, text=b, width=5, height=2,font=("Times New Roman",16,"bold"), fg="blue", bg="white", command=cmd).grid(row=row, column=col)
    col += 1
    
    if col > 3:
        col = 0
        row += 1
        
Button(root, text="=", width=5, height=2,font=("Times New Roman",16,"bold"),fg="red", bg="white", command=equal).grid(row=5,column=3)
Button(root,text="Del",width=5,height=2,font=("Times New Roman",16,"bold"), fg="green", bg="white", command=delete).grid(row=1, column=2)

root.mainloop()

from tkinter import *

window=Tk()
window.title("Convertor")

def from_GB():
    MB=float(e2_value.get())*1000
    KB=MB*1000
    B=KB*1000
    t1.insert(END,MB)
    t2.insert(END,KB)
    t3.insert(END,B)

e1=Label(window,text="Enter value in GB")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

b1=Button(window,text="Convert",command=from_GB)
b1.grid(row=0,column=2)

l1 = Label(window,text="MB")
l1.grid(row=1,column=0)

l2 = Label(window,text="KB")
l2.grid(row=1,column=1)

l3 = Label(window,text="B")
l3.grid(row=1,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=2,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=2,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=2)

window.mainloop()
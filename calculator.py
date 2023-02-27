from tkinter import *

root = Tk()
root.title("Calculator")


first = None
operator = None
second = None
l = None

e1 = Entry(root)
e1.grid(row=0,column=0,columnspan=2,rowspan=2)
e2 = Entry(root)
e2.grid(row=0,column=2,columnspan=2,rowspan=2)


def button_click(i):
    e1.insert(END,i)

def clearAll():
    e1.delete(0,END)
    e2.delete(0,END)

def calculateIt():
    expression = e1.get()
    if len(expression) == 0:
        clearAll()
        return

    val = eval(expression)
    e2.delete(0,END)
    e2.insert(0,str(val))

b0 = Button(root,text="0",command = lambda : button_click(0))
b1 = Button(root,text="1",command = lambda : button_click(1))
b2 = Button(root,text="2",command = lambda : button_click(2))
b3 = Button(root,text="3",command = lambda : button_click(3))
b4 = Button(root,text="4",command = lambda : button_click(4))
b5 = Button(root,text="5",command = lambda : button_click(5))
b6 = Button(root,text="6",command = lambda : button_click(6))
b7 = Button(root,text="7",command = lambda : button_click(7))
b8 = Button(root,text="8",command = lambda : button_click(8))
b9 = Button(root,text="9",command = lambda : button_click(9))

ba = Button(root,text='+',command = lambda : button_click('+'))
bm = Button(root,text='*',command = lambda : button_click('*'))
bs = Button(root,text='-',command = lambda : button_click('-'))
bd = Button(root,text='/',command = lambda : button_click('/'))
bclear = Button(root,text='C',command = clearAll)
bequal = Button(root,text='=',command = calculateIt)

b0.grid(row=2,column=0,sticky='nsew')
b1.grid(row=2,column=1,sticky="nsew")
b2.grid(row=2,column=2,sticky="nsew")
b3.grid(row=2,column=3,sticky="nsew")

b4.grid(row=3,column=0,sticky="nsew")
b5.grid(row=3,column=1,sticky="nsew")
b6.grid(row=3,column=2,sticky="nsew")
b7.grid(row=3,column=3,sticky="nsew")

b8.grid(row=4,column=0,sticky="nsew")
b9.grid(row=4,column=1,sticky="nsew")
ba.grid(row=4,column=2,sticky="nsew")
bm.grid(row=4,column=3,sticky="nsew")

bs.grid(row=5,column=0,stick='nsew')
bd.grid(row=5,column=1,stick='nsew')
bclear.grid(row=5,column=2,stick='nsew')
bequal.grid(row=5,column=3,stick='nsew')

root.mainloop()
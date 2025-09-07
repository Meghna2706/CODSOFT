'''simple calculator with basic arithmetic operations.'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#window
window=Tk()
window.title("Calculator")
window.geometry('400x300')
window.resizable(0,0)

#two variables
var1=StringVar()
var2=StringVar()

#selected item in combobox 
def sel():
    value=combo.get()

#list items of operations
list=[("Addition","+"),("Subtraction","-"),("Multiplication","*"),("Integer Division","//"),("Float Division","/"),("Remainder","%"),("Power","**")]
display=[item[0] for item in list]

#combobox initialization for displaying items
combo=ttk.Combobox(window,values=display)
combo.bind("<<ComboboxSelected>>",sel)
combo.grid(column=2,row=2,padx=5, pady=5)
combo.current()

#Calculation method
def compute():
    try:

        #Getting the values entered in the entry box
        val1=var1.get()
        val2=var2.get()

        #Converting the String values(entered) to the float
        x=float(val1)
        y=float(val2)
        val=combo.get()
        operator=None

        #Getting only the operator not the text from the list items
        for display,op in list:
            if val==display:
                operator=op

        #Comparision
        if operator=='+':
            z=x+y
        elif operator=='-':
            z=x-y
        elif operator=='*':
            z=x*y
        elif operator=='//':
            z=x//y
        elif operator=='/':
            z=x/y
        elif operator=='%':
            z=x%y
        elif operator=='**':
            z=x**y
        messagebox.showinfo("Output",val1+operator+val2+'='+str(z))
    except ValueError:
        messagebox.showinfo("Error","Invalid Input, Enter correct value")

#Label for first value
l1=Label(window,text='Enter first value:')
#Entry for first value
e1=Entry(window,width=10,textvariable=var1)
#Label for second value
l2=Label(window,text='Enter second value:')
#Entry for second value
e2=Entry(window,width=10,textvariable=var2)

#Label for option selection
l3=Label(window,text='Choose the option')

#Button for calculation
b=Button(window,text='Calculate',command=compute,bg="lightblue",fg="black")

#Adjusting the labels,entry and button
l1.grid(column=1,row=0, padx=5, pady=5)
e1.grid(column=2,row=0, padx=5, pady=5)
l2.grid(column=1,row=1, padx=5, pady=5)
e2.grid(column=2,row=1, padx=5, pady=5)
l3.grid(column=1,row=2, padx=5, pady=5)
b.grid(column=2,row=3, padx=5, pady=5)

#Run GUI
window.mainloop()
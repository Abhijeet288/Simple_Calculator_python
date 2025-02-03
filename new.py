from tkinter import *
win = Tk()  #creates an instance of the tkinter

win.title('Calculator')  #used for keeping title for the application
win.geometry('450x450')     #used to keep the size of the application
win.resizable(0,0)

#function for all the buttons except = and clear.
def btn_click(item):
    global expression
    expression=expression+str(item)  #append the values to the text-input field.
    input_txt.set(expression)



#function for clear button.
def bt_clear():
    global expression
    expression=""
    input_txt.set("")

#function for = button
def btn_equal():
    global expression       #making 'expression' global to access inside the function
    result=str(eval(expression))  #convert the operation in string and storing it in a variable
    input_txt.set(result)   #for showing the output
    expression=""           #it will again assign the expression as null.


expression=''
input_txt=StringVar()


input_frame=Frame(win,width=312,height=50)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,font=('arial',18,'bold') ,width=45,justify=RIGHT, textvariable=input_txt)
input_field.grid(row=0,column=0)

input_field.pack(ipady=10)

btns_frame=Frame(win,width=310,height=270)
btns_frame.pack()


clear=Button(btns_frame,text='C',width=38,height=3,command=lambda:bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide=Button(btns_frame,text='/',width=10,height=3,command=lambda:btn_click('/ ')).grid(row=0, column=3, pady=1,padx=1)

seven=Button(btns_frame,text='7',width=10,height=3,command=lambda:btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight=Button(btns_frame,text='8',width=10,height=3,command=lambda:btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
night=Button(btns_frame,text='9',width=10,height=3,command=lambda:btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply=Button(btns_frame,text='*',width=10,height=3,command=lambda:btn_click('*')).grid(row=1, column=3, padx=1, pady=1)


four=Button(btns_frame,text='4',width=10,height=3,command=lambda:btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five=Button(btns_frame,text='5',width=10,height=3,command=lambda:btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six=Button(btns_frame,text='6',width=10,height=3,command=lambda:btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus=Button(btns_frame,text='-',width=10,height=3,command=lambda:btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

one=Button(btns_frame,text='1',width=10,height=3,command=lambda:btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two=Button(btns_frame,text='2',width=10,height=3,command=lambda:btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three=Button(btns_frame,text='3',width=10,height=3,command=lambda:btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus=Button(btns_frame,text='+',width=10,height=3,command=lambda:btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

zero=Button(btns_frame,text='0',width=24,height=3,command=lambda:btn_click(0)).grid(row=4, column=0,columnspan=2, padx=1, pady=1)
point=Button(btns_frame,text='.',width=10,height=3,command=lambda:btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal=Button(btns_frame,text='=',width=10,height=3,command=lambda:btn_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()  #makes our application visible

from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ''
    text_input.set('0')

def btnEqual():
    global operator
    equal = str(eval(operator))
    text_input.set(equal)
    #operator = ''


cal = Tk()
cal.title('Calculator')
cal.resizable(0,0)
operator = ''
text_input = StringVar()

txtDispaly = Entry(cal,font=('arial',20,'bold'), textvariable = text_input, bd = 25 , insertwidth = 4 ,
                   bg = "brown" , justify = 'right').grid(columnspan =4)


btn1 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '1', command = lambda:btnClick(1),bg ='grey').grid(row = 1, column = 0)

btn2 = Button(cal,padx = 8, bd = 10, fg = 'black', font=('arial',20,'bold'),
              text = '2',command = lambda:btnClick(2),bg ='grey').grid(row = 1, column = 1)

btn3 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '3',command = lambda:btnClick(3),bg ='grey').grid(row = 1, column = 2)
#========================================================================

btn4 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '4',command = lambda:btnClick(4),bg ='grey').grid(row = 2, column = 0)

btn5 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '5',command = lambda:btnClick(5),bg ='grey').grid(row = 2, column = 1)

btn6 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '6',command = lambda:btnClick(6),bg ='grey').grid(row = 2, column = 2)

#=========================================================================

btn7 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '7',command = lambda:btnClick(7),bg ='grey').grid(row = 3, column = 0)

btn8 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '8',command = lambda:btnClick(8),bg ='grey').grid(row = 3, column = 1)

btn9 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '9',command = lambda:btnClick(9),bg ='grey').grid(row = 3, column = 2)

#=========================================================================

Addition = Button(cal,padx = 9, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '+',bg ='orange',command = lambda:btnClick('+')).grid(row = 1, column = 3)

Subtraction = Button(cal,padx =12, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '-',bg ='orange',command = lambda:btnClick('-')).grid(row = 2, column = 3)

Multiply = Button(cal,padx = 9, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = 'x',bg ='orange',command = lambda:btnClick('*')).grid(row = 3, column = 3)

Divide = Button(cal,padx = 9, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '÷',bg ='orange',command = lambda:btnClick('/')).grid(row = 4, column = 3)

#==========================================================================

Equals = Button(cal,padx =8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '=',bg ='aqua',command = btnEqual).grid(row = 4, column = 2)

btn0 = Button(cal,padx = 8, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = '0',command = lambda:btnClick(0),bg ='grey').grid(row = 4, column = 1)

Clearscreen = Button(cal,padx = 6, bd = 10 , fg = 'black', font=('arial',20,'bold'),
              text = 'C',bg ='red',command = btnClear).grid(row = 4, column = 0)

cal.mainloop()
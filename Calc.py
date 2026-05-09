from tkinter import *
import math
root = Tk()
root.title("Calculator")
res = 0
Calculation =""
def addition(*args):
    global res
    for i in range(len(args)):
        res += args[i]
    return res
def substraction(*args):
    global res
    for i in range(len(args)):
        res += args[i]
    return res
def product(*args):
    global res
    for i in range(len(args)):
        res *= args[i]
    return res
def division(*args):
    global res
    for i in range(len(args)):
        res += args[i]
    return res
# fuction to help identify numbers and operators
def print_this(a):
    global Calculation
    if(a == "back"):
        Calculation = Calculation[:len(Calculation)]
    else:
        Calculation = Calculation + a
        text_update(Calculation)

#Display Update function
def text_update(a):
    textvar.set(a)

#Choose operators
def choose_op(x):
    match x:
        case 1:
            return "+"
        case 2:
            return "-"
        case 3:
            return "X"
        case 4:
            return "/"
        case 5:
            return "("
        case 6:
            return ")"
        case 7:
            return "^"
        case 8:
            return "back"

#Syntax Error
def error(x):
    if(x in operators):
        next_str = Calculation[Calculation.index(x)+1]
        if(next_str not in numbers or next_str !="(" or x == ")" ):
            return False
        else:
            return True
        
#Divide the Equation into bracket and non bracket parts
def divide_equation():
    x = 0


#Generate Output
def output():
    for i in Calculation:
        if (error(i)==False):
            text_update("Syntax Error!!")
            





#MAIN UI#
#Major Variables#
x_cords = 500
normal_width=50
normal_height=90
y_cords=200
display_height=60
display_width_factor = 8
op_per_row= 4
operators = ["+","-","X","/","(",")","^"]
numbers=[1,2,3,4,5,6,7,8,9,0]

#Display Frame UI
Display = Frame(root,bg = "lightgrey",bd=3,relief = "sunken",)
Display.place(x= (x_cords+normal_width),y=(y_cords-display_height),width=normal_width*display_width_factor, height=display_height,)
textvar = StringVar(value="Waiting...")
Dis = Label(Display, text="",textvariable=textvar, bg="lightgrey")
Dis.pack(pady=10)

#NumbersUI
def assign(a):
    for i in range(10):
        a = Button(root,text=i)
        a.config( command= lambda x=i: print_this(str(x)))
        deter=0
        if(i==0):
            a.place(x=x_cords+normal_width*4,y=y_cords,height=normal_height*3,width=normal_width)
        else:
            if(i%3==0):
                deter = 3
            a.place(x=(x_cords+(i%3)*normal_width + normal_width*deter),y=(y_cords + normal_height*(math.ceil(i/3)-1)),height=90, width=normal_width)
buttons = []
for i in range(10):
    buttons.append("button_" + str(i)) 
assign(str(buttons[i]))


#OperatorsUI
for i in range(1,9):
        deter=0
        op= choose_op(i)
        a = Button(root,text=op)
        a.config( command= lambda x=op: print_this(str(x)))
        if(i%4==0):
            deter = 4
        a.place(x=((x_cords + normal_width*op_per_row)+ (i%4) * normal_width + normal_width*deter),y=(y_cords + normal_height*(math.ceil(i/4)-1)),height=normal_height, width=normal_width)


#Equals_to Opetator UI
equals_to = Button(root,text="=",font=("",20,"bold"),command = output)
equals_to.place(x=x_cords + normal_width*5, y=y_cords+normal_height*2, height=normal_height, width=normal_width*4)
      
root.mainloop()
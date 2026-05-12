
from tkinter import *
root = Tk()
root.title("Calculator")

#global variables
res = 0
Calculation =""
operators_used = []
equations= []


# fuction to help identify numbers and operators
def print_this(a):
    global Calculation
    if(a == "back"):
        Calculation = Calculation[:len(Calculation)-1]
        text_update(Calculation)
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
def error():
    global Calculation
    error = False
    prev_index = -1
    for x in Calculation:
        prev_index +=1
        if(x in operators[0:5]):
            if(x == Calculation[-1]):
                error = True
            else:
                #print(prev_index)
                next_str = Calculation[prev_index + 1]
                if((next_str not in numbers and next_str !="(")):
                    error = True
    return error
        
#Divide the Equation into bracket and non bracket parts
def divide_equations(main_eq):
    global equations
    global operators_used
    local_Calculation = main_eq
    global a
    index_counter = 0
    a = 0 # "a" keeps the starting index of new equation
    x = 0
    for i in local_Calculation:
        index_counter +=1
                
        if (i in operators):    
            x = local_Calculation[a:].index(i) + a

        if(i == "^"): # Solving the power equations here.
            value = 1
            decimal_base = 0
            decimal = False
            for i in local_Calculation[a:x]:
                if(i =="."):
                    decimal = True
                if(decimal):
                    decimal_base += 1
            #print(decimal_base,"base")
            base = float(local_Calculation[a:x])
            a = x+1
            
            for i in local_Calculation[a:]:
                if(i in operators[0:6]):
                    index_of_power_end = local_Calculation[a:].index(i) + a
                else: 
                    index_of_power_end = len(local_Calculation[a:]) + a
                    #print(index_of_power_end)
                
            value = base ** int(local_Calculation[a:index_of_power_end])
            
            equations.append(value)
            #print(equations,"equations")
            #print(operators_used, "operators")

        if (i in operators and i !="(" and i!= ")" and i!="^"):
            operators_used.append(i)
            equations.append(local_Calculation[a:x])
            #print(local_Calculation[a:x])
            a = x + 1
            

    random = -1
    for i in reversed(local_Calculation):
        random += 1
        if(i in operators):
            print(local_Calculation[len(local_Calculation) - random :],"heram")
            equations.append(local_Calculation[len(local_Calculation) - random :])
            break
    print(equations, "eqtn")
    print(operators_used,"op")


#compute the divided equations
def main_compute(num):
    global res
    #print(operators_used)
    for i in operators_used:
        eq1 = float(equations[num*2 - 2])
        eq2 = float(equations[num*2 - 1])
        print(i)
        match i:
            case "/":
                if(eq2 == 0):
                    text_update("Math Error!")
                    res = 1
                    break
                else:
                    return (eq1/eq2)
            case "+":
                print(eq1,eq2)
                return ( eq1 + eq2 )
            case "-":
                return (eq1 - eq2)
            case "X":
                return (eq1 * eq2)
            


def compute():
    for i in range(len(operators_used)):
        equations[i]=main_compute(i+1)



#Generate Output
def output():
    global Calculation
    global res
    if (error()):
        text_update("Syntax Error!")
        return
    #print(equations, "h1")
    divide_equations(Calculation)
    compute()
    #print(operators_used)
    #print(equations)
    #print(Test_Calculation)
    #print(res)
    if(res != 1):
        Calculation = str(equations[0])
        text_update(Calculation)
        equations.clear()
        operators_used.clear()

    res = 0



#MAIN UI#
#Major Variables#
operators = ["+","-","X","/","^",")","("]
numbers=["1","2","3","4","5","6","7","8","9","0"]
x_cords = 500
normal_width=50
normal_height=90
y_cords=200
display_height=60
op_per_row = (len(operators)+1)/2
num_per_row = 3
display_width_factor = op_per_row + num_per_row + 1



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
        deter = 0
        if(i==0):
            a.place(x=x_cords+normal_width*4,y=y_cords,height=normal_height*3,width=normal_width)
        else:
            if(i%3==0):
                deter = 3
            a.place(x=(x_cords+(i%3)*normal_width + normal_width*deter),y=(y_cords + normal_height*(int(i/3)- deter*1/3 )),height=90, width=normal_width)
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
        a.place(x=((x_cords + normal_width*op_per_row)+ (i%4) * normal_width + normal_width*deter),y=(y_cords + normal_height*(int(i/4)-deter*1/4)),height=normal_height, width=normal_width)


#Equals_to Opetator UI
equals_to = Button(root,text="=",font=("",20,"bold"),command = output)
equals_to.place(x=x_cords + normal_width*5, y=y_cords+normal_height*2, height=normal_height, width=normal_width*4)
      
root.mainloop()
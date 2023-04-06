from tkinter import*
from tkinter import ttk
from ttkthemes import ThemedTk
import math

window = ThemedTk(theme='scidgreen')
window.title("Your Personal Calculator")
window.geometry('350x400')
window.configure(themebg="ubuntu")
result=""
equation=StringVar()

def delete():
    global equation, result,txtbox
    txtbox.delete(len(txtbox.get())-1)
    result=equation.get()


def clear():
    global result,equation
    result=""
    equation.set("")
def Close():
    window.destroy()
def press(x):
    global result ,equation
    result= result+str(x)
    equation.set(result)
def equal():
    try:
        global result,equation
        conclusion=str(eval(result))
        equation.set(conclusion)
        result=""
    except:
        equation.set("Error")
        result=""
txtbox=Entry(window,fg="black",text=equation,bg="white",width=17,font=("Aqua",30))
txtbox.place(x=0,y=0)

butclear= ttk.Button(window, text="CLEAR", cursor="exchange",command=clear)
butclear.place(x=0, y=50,width=80,height=35)

butplus = ttk.Button(window, text="➕", cursor="exchange",command=lambda :press("+"))
butplus.place(x=269, y=100,width=80,height=55)

butminus = ttk.Button(window, text="➖", cursor="exchange",command=lambda :press("-"))
butminus.place(x=269, y=160,width=80,height=55)

butmultiply = ttk.Button(window, text="✖", cursor="exchange",command=lambda :press("*"))
butmultiply.place(x=269, y=220,width=80,height=55)

butdivide = ttk.Button(window, text="➗", cursor="exchange",command=lambda :press("/"))
butdivide.place(x=269, y=280,width=80,height=55)

butnum1 = ttk.Button(window, text="1", cursor="exchange",command=lambda :press(1))
butnum1.place(x=0, y=100,width=80,height=55)

butnum2 = ttk.Button(window, text="2", cursor="exchange",command=lambda :press(2))
butnum2.place(x=90, y=100,width=80,height=55)

butnum3 = ttk.Button(window, text="3", cursor="exchange",command=lambda :press(3))
butnum3.place(x=180, y=100,width=80,height=55)

butnum4 = ttk.Button(window, text="4", cursor="exchange",command=lambda :press(4))
butnum4.place(x=0, y=160,width=80,height=55)

butnum5 = ttk.Button(window, text="5", cursor="exchange",command=lambda :press(5))
butnum5.place(x=90, y=160,width=80,height=55)

butnum6 = ttk.Button(window, text="6", cursor="exchange",command=lambda :press(6))
butnum6.place(x=180, y=160,width=80,height=55)

butnum7= ttk.Button(window, text="7", cursor="exchange",command=lambda :press(7))
butnum7.place(x=0, y=220,width=80,height=55)

butnum8= ttk.Button(window, text="8", cursor="exchange",command=lambda :press(8))
butnum8.place(x=90, y=220,width=80,height=55)

butnum9= ttk.Button(window, text="9", cursor="exchange",command=lambda :press(9))
butnum9.place(x=180, y=220,width=80,height=55)

butnum0= ttk.Button(window, text="0", cursor="exchange",command=lambda :press(0))
butnum0.place(x=90, y=280,width=80,height=55)

butequal= ttk.Button(window, text="=", cursor="exchange",command=equal)
butequal.place(x=180, y=340,width=170,height=55)

butparenthesis1= ttk.Button(window, text="﹙", cursor="exchange",command=lambda :press("("))
butparenthesis1.place(x=0, y=280,width=80,height=55)

butparenthesis2= ttk.Button(window, text="﹚", cursor="exchange",command=lambda :press(")"))
butparenthesis2.place(x=180, y=280,width=80,height=55)

butpower= ttk.Button(window, text="^", cursor="exchange",command=lambda :press("**"))
butpower.place(x=90, y=50,width=80,height=35)

butsquareroot= ttk.Button(window, text="√", cursor="exchange",command=lambda :press("math.sqrt("))
butsquareroot.place(x=180, y=50,width=80,height=35)

butclose= ttk.Button(window, text="CLOSE", cursor="exchange",command=Close)
butclose.place(x=0, y=340,width=80,height=55)

butdelete= ttk.Button(window, text="Delete", cursor="exchange",command=delete)
butdelete.place(x=269, y=50,width=80,height=35)


window.mainloop()
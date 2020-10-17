from tkinter import *
from tkinter import messagebox
import math

screen =Tk()
screen.title('Calculator')
screen.configure(bg='grey')
screen.iconbitmap('cali.ico')
#screen.geometry('400x390')
screen.maxsize(width='400',height='360')
screen.minsize(width='400',height='360')

def clear():
    global storagevariable
    storagevariable = ''
    text.set(storagevariable)

def click(num):
    global storagevariable
    storagevariable += str(num)
    text.set(storagevariable)

def equal():
    global storagevariable
    result = eval(storagevariable)
    storagevariable =str(result)
    text.set(result)

def sinfun():
    global storagevariable
    try:
        result = math.sin(eval(text.get()))
        storagevariable = str(result)
        text.set(result)
    except:
        messagebox.showinfo('Notification','Try Again!',parent=screen)

def cosfun():
    global storagevariable
    try:
        result = math.cos(eval(text.get()))
        storagevariable = str(result)
        text.set(result)
    except:
        messagebox.showinfo('Notification','Try Again!',parent=screen)

def tanfun():
    global storagevariable
    try:
        result = math.tan(eval(text.get()))
        storagevariable = str(result)
        text.set(result)
    except:
        messagebox.showinfo('Notification','Try Again!',parent=screen)

def logfun():
    global storagevariable
    try:
        result = math.log(eval(text.get()))
        storagevariable = str(result)
        text.set(result)
    except:
        messagebox.showinfo('Notification','Try Again!',parent=screen)

def sqrtfun():
    global storagevariable
    try:
        result = math.sqrt(eval(text.get()))
        storagevariable = str(result)
        text.set(result)
    except:
        messagebox.showinfo('Notification','Try Again!',parent=screen)
################################HOVER Function################################################
def on_hover7(e):
    btn7.configure(bg='lightblue')

def off_hover7(e):
    btn7.configure(bg='white')

def on_hover8(e):
    btn8.configure(bg='lightblue')

def off_hover8(e):
    btn8.configure(bg='white')

def on_hover9(e):
    btn9.configure(bg='lightblue')

def off_hover9(e):
    btn9.configure(bg='white')

def on_hover6(e):
    btn6.configure(bg='lightblue')

def off_hover6(e):
    btn6.configure(bg='white')

def on_hover5(e):
    btn5.configure(bg='lightblue')

def off_hover5(e):
    btn5.configure(bg='white')

def on_hover4(e):
    btn4.configure(bg='lightblue')

def off_hover4(e):
    btn4.configure(bg='white')

def on_hover3(e):
    btn3.configure(bg='lightblue')

def off_hover3(e):
    btn3.configure(bg='white')

def on_hover2(e):
    btn2.configure(bg='lightblue')

def off_hover2(e):
    btn2.configure(bg='white')

def on_hover1(e):
    btn1.configure(bg='lightblue')

def off_hover1(e):
    btn1.configure(bg='white')

def on_hover0(e):
    btn0.configure(bg='lightblue')

def off_hover0(e):
    btn0.configure(bg='white')

def on_hoveradd(e):
    btnadd.configure(bg='lightblue')

def off_hoveradd(e):
    btnadd.configure(bg='white')

def on_hoversub(e):
    btnsub.configure(bg='lightblue')

def off_hoversub(e):
    btnsub.configure(bg='white')

def on_hovermul(e):
    btnmul.configure(bg='lightblue')

def off_hovermul(e):
    btnmul.configure(bg='white')

def on_hoverdiv(e):
    btndiv.configure(bg='lightblue')

def off_hoverdiv(e):
    btndiv.configure(bg='white')

def on_hoverequal(e):
    btnequal.configure(bg='lightblue')

def off_hoverequal(e):
    btnequal.configure(bg='white')

def on_hoverclear(e):
    btnclear.configure(bg='lightblue')

def off_hoverclear(e):
    btnclear.configure(bg='white')

def on_hoversin(e):
    btnsin.configure(bg='lightblue')

def off_hoversin(e):
    btnsin.configure(bg='white')

def on_hovercos(e):
    btncos.configure(bg='lightblue')

def off_hovercos(e):
    btncos.configure(bg='white')

def on_hovertan(e):
    btntan.configure(bg='lightblue')

def off_hovertan(e):
    btntan.configure(bg='white')

def on_hoversqrt(e):
    btnsqrt.configure(bg='lightblue')

def off_hoversqrt(e):
    btnsqrt.configure(bg='white')

def on_hoverlog(e):
    btnlog.configure(bg='lightblue')

def off_hoverlog(e):
    btnlog.configure(bg='white')

text = StringVar()
storagevariable=''

entry0=Entry(screen,bg='orange',font=('arial',20,'italic'),bd='10',justify='right',textvariable=text)
entry0.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(7),
              activebackground='black',activeforeground='white')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(8),activebackground='black',activeforeground='white')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(9),activebackground='black',activeforeground='white')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click('+'),activebackground='black',activeforeground='white')
btnadd.grid(row=1,column=3)

btnsin = Button(screen,text='sin',font=('arial',10),bd='10',padx=15,pady=15,command=sinfun,activebackground='black',activeforeground='white')
btnsin.grid(row=0,column=4)

btn4 = Button(screen,text='4',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(4),activebackground='black',activeforeground='white')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(5),activebackground='black',activeforeground='white')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(6),activebackground='black',activeforeground='white')
btn6.grid(row=2,column=2)

btnsub = Button(screen,text='-',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click('-'),activebackground='black',activeforeground='white')
btnsub.grid(row=2,column=3)

btntan = Button(screen,text='tan',font=('arial',10),bd='10',padx=15,pady=15,command=tanfun,activebackground='black',activeforeground='white')
btntan.grid(row=2,column=4)

btncos = Button(screen,text='cos',font=('arial',10),bd='10',padx=15,pady=15,command=cosfun,activebackground='black',activeforeground='white')
btncos.grid(row=1,column=4)

btn3 = Button(screen,text='3',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(3),activebackground='black',activeforeground='white')
btn3.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(2),activebackground='black',activeforeground='white')
btn2.grid(row=3,column=1)

btn1 = Button(screen,text='1',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(1),activebackground='black',activeforeground='white')
btn1.grid(row=3,column=2)

btnmul = Button(screen,text='*',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click('*'),activebackground='black',activeforeground='white')
btnmul.grid(row=3,column=3)

btnsqrt = Button(screen,text='sqrt',font=('arial',10),bd='10',padx=15,pady=15,command=sqrtfun,activebackground='black',activeforeground='white')
btnsqrt.grid(row=3,column=4)

btn0 = Button(screen,text='0',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click(0),activebackground='black',activeforeground='white')
btn0.grid(row=4,column=0)

btnclear = Button(screen,text='C',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:clear(),activebackground='black',activeforeground='white')
btnclear.grid(row=4,column=1)

btnequal = Button(screen,text='=',font=('arial',10),bd='10',padx=18,pady=15,command=equal,activebackground='black',activeforeground='white')
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text='/',font=('arial',10),bd='10',padx=18,pady=15,command=lambda:click('/'),activebackground='black',activeforeground='white')
btndiv.grid(row=4,column=3)

btnlog = Button(screen,text='log',font=('arial',10),bd='10',padx=15,pady=15,command=logfun,activebackground='black',activeforeground='white')
btnlog.grid(row=4,column=4)

btn7.bind('<Enter>',on_hover7)
btn7.bind('<Leave>',off_hover7)

btn8.bind('<Enter>',on_hover8)
btn8.bind('<Leave>',off_hover8)

btn9.bind('<Enter>',on_hover9)
btn9.bind('<Leave>',off_hover9)

btn6.bind('<Enter>',on_hover6)
btn6.bind('<Leave>',off_hover6)

btn5.bind('<Enter>',on_hover5)
btn5.bind('<Leave>',off_hover5)

btn4.bind('<Enter>',on_hover4)
btn4.bind('<Leave>',off_hover4)

btn3.bind('<Enter>',on_hover3)
btn3.bind('<Leave>',off_hover3)

btn2.bind('<Enter>',on_hover2)
btn2.bind('<Leave>',off_hover2)

btn1.bind('<Enter>',on_hover1)
btn1.bind('<Leave>',off_hover1)

btn0.bind('<Enter>',on_hover0)
btn0.bind('<Leave>',off_hover0)

btnadd.bind('<Enter>',on_hoveradd)
btnadd.bind('<Leave>',off_hoveradd)

btnsub.bind('<Enter>',on_hoversub)
btnsub.bind('<Leave>',off_hoversub)

btnmul.bind('<Enter>',on_hovermul)
btnmul.bind('<Leave>',off_hovermul)

btndiv.bind('<Enter>',on_hoverdiv)
btndiv.bind('<Leave>',off_hoverdiv)

btnclear.bind('<Enter>',on_hoverclear)
btnclear.bind('<Leave>',off_hoverclear)

btnequal.bind('<Enter>',on_hoverequal)
btnequal.bind('<Leave>',off_hoverequal)

btnsin.bind('<Enter>',on_hoversin)
btnsin.bind('<Leave>',off_hoversin)

btncos.bind('<Enter>',on_hovercos)
btncos.bind('<Leave>',off_hovercos)

btntan.bind('<Enter>',on_hovertan)
btntan.bind('<Leave>',off_hovertan)

btnsqrt.bind('<Enter>',on_hoversqrt)
btnsqrt.bind('<Leave>',off_hoversqrt)

btnlog.bind('<Enter>',on_hoverlog)
btnlog.bind('<Leave>',off_hoverlog)

screen.mainloop()

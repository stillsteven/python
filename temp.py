from tkinter import*
import random

a = {}
win = {-3:"你贏",-2:"平手",-1:"你輸",0:"平手",1:"你贏",2:"平手",3:"你輸"}

def join():
    list(e1.get())[int(e2.get())]=e3.get()
    e2.delete(0,END)
    e3.delete(0,END)

def show():  
    print(a)
    
def play():
    b = random.randint(1,4)
    h = b - int(e4.get()) 
    t8 = Label(y,text=(b)).grid(row=2,column=3)
    t9 = Label(y,text=(a[int(e4.get())],"與",a[b])).grid(row=3,column=1)
    t0 = Label(y,text=(win[h])).grid(row=3,column=3)
    
def again():
    e4.delete(0,END)
    t8 = Label(y,text=" ").grid(row=2,column=3)
    t9 = Label(y,text="                 ").grid(row=3,column=1)
    t0 = Label(y,text="           ").grid(row=3,column=3)

#====================================================================================================
x = Tk()

x.title("GUI檢覈")
x.geometry("300x160")
label = Label(x,text="Lebel字典準備").grid(row=0,column=2)

t1 = Label(x,text="字典名稱").grid(row=1)
t2 = Label(x,text="對應鍵").grid(row=2)
t3 = Label(x,text="對應值").grid(row=3)

e1 = Entry(x)
e2 = Entry(x)
e3 = Entry(x)

e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)

b1 = Button(x,text="確認加入",command=join)
b2 = Button(x,text="建立完成",command=x.destroy)
b3 = Button(x,text="test",command=show)

b1.grid(row=4,column=0)
b2.grid(row=4,column=2)
b3.grid(row=4,column=3)

x.mainloop()
#=================================================================================================
y = Tk()

y.title("GUI遊戲")
y.geometry("400x160")
t4 = Label(y,text="遊戲進行中").grid(row=0,column=2)
t5 = Label(y,text="你出").grid(row=1,column=1)
t6 = Label(y,text="電腦出").grid(row=1,column=3)
t7 = Label(y,text="結果").grid(row=3, column=0)

e4 = Entry(y)
e4.grid(row=2,column=1)

b4 = Button(y,text="猜",command=play)
b5 = Button(y,text="再玩一次",command=again)
b6 = Button(y,text="結束",command=y.destroy)

b4.grid(row=2,column=2)
b5.grid(row=4,column=1)
b6.grid(row=4,column=2)

y.mainloop()

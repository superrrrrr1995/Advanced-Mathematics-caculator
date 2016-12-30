#coding=utf-8
from Tkinter import *
from sympy import *

import time
import os
import sqlite3
def sql(f,d1,d2,n):
    try:
        x=Symbol('x')
        f=eval(f)
        a1=str(f)
        a2=str(diff(f,x))
        a3=str(integrate(f,x))
        a4=str(integrate(f,(x,d1,d2)))
        a5=str(solve(f,x))
        a6=str(f.series(x,0,n))

    except:
        pass
    
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table function ( function primary key, 解析式 varchar(10), 定义域 varchar(10),导函数 varchar(10),不定积分 varchar(10) ,定积分 varchar(10) ,零点 varchar(10) ,泰勒展开 varchar(10)  )""")
    except:
        pass
    try:
        for t in[('%s,%s,%s'%(a1,d1,d2),a1,'[%s,%s]'%(d1,d2),a2,a3,a4,a5,a6)]:    
            cx.execute("insert into function values (?,?,?,?,?,?,?,?)", t)
    except:
        pass
    cx.commit()

def zjm2():
    c1=Button(math3,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    math3.destroy()
    os.system("menu.py")

def b():
    ans=[0 for m in range(6)]
    ans[0]=limit(eval(e1[0].get()), x,eval(e2[0].get()))
    ans[1]=diff(eval(e1[1].get()), x)
    ans[2]=diff(eval(e1[2].get()), x,eval(e2[2].get()))
    ans[3]=(eval(e1[3].get()).series(x,0,eval(e2[3].get())))
    ans[4]=integrate(eval(e1[4].get()), x)
    ans[5]=integrate(eval(e1[5].get()), (x,eval(e2[5].get()),eval(e3[5].get())))

    sql(e1[0].get(),0,1,5)
    sql(e1[1].get(),0,1,5)
    sql(e1[2].get(),0,1,5)
    sql(e1[3].get(),0,1,eval(e2[3].get()))
    sql(e1[4].get(),0,1,5)
    sql(e1[5].get(),eval(e2[5].get()),eval(e3[5].get()),5)
    
    
    for i in range(len(ans)):
        Label(math3,text='答案:',font=('',20),fg='red',bg='lightblue').place(x=250,y=140+80*i)
        Label(math3,text=ans[i],font=('',20),fg='red',bg='lightblue').place(x=340,y=140+80*i)

x=Symbol("x")
math3 = Tk()
canvas = Canvas(math3,width = 1000, height = 666)

im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
c2=Button(math3,image=im3,command=zjm2).place(x=820,y=600)
canvas.create_image(500,333,image = im)
xt=canvas.create_text(500,50,text='微积分运算',fill='green',font=('', 30))
a1=['极限','微分','高阶微分','泰勒展开','不定积分','定积分']
c1=['(1+1/x)','sin(x)','x**3','exp(x)','1/x','x']
a2=['x->','','阶数:','阶数:','','下限:']
c2=['oo','','6','5','','0']
a3=['','','','','','上限：']
c3=['','','','','','10']
e1=[0 for i in range(10)]
e2=[0 for i in range(10)]
e3=[0 for i in range(10)]
for i in range(len(a1)):
    Label(math3,text='%d.'%(i+1),fg='brown',font=('',20)).place(x=40,y=100+80*i)
    Label(math3,text=a1[i],fg='brown',bg='yellow',font=('',20)).place(x=70,y=100+80*i)
    Label(math3,text='函数:',fg='blue',bg='yellow',font=('',20)).place(x=250,y=100+80*i)
    e1[i]=Entry(math3,width=15,font=('',20 ))
    e1[i].insert(END,c1[i])
    e1[i].place(x=340,y=100+80*i)
    if a2[i]!='':
        Label(math3,text=a2[i],fg='blue',bg='yellow',font=('',20)).place(x=600,y=100+80*i)
        e2[i]=Entry(math3,width=3,font=('',20 ))
        e2[i].place(x=680,y=100+80*i)
        e2[i].insert(END,c2[i])
    
    if a3[i]!='':
        Label(math3,text=a2[i],fg='blue',bg='yellow',font=('',20)).place(x=750,y=100+80*i)
        e3[i]=Entry(math3,width=3,font=('',20 ))
        e3[i].place(x=830,y=100+80*i)
        e3[i].insert(END,c3[i])
Button(math3,width=15,text='计算',command=b,fg='red',font=('',20)).place(x=400,y=600)
        
canvas.pack()
mainloop()

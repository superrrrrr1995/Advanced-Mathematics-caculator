#coding=utf-8
from Tkinter import *
from numpy import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import time
import os
import sqlite3

def sql_graph(c1,c2,c3,c4,c5):
    
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table graph ( 函数 primary key, 解析式 varchar(10), 定义域 varchar(10),坐标类型 varchar(10), 图像路径 varchar(10))""")
    except:
        pass
    try:
        for t in[(c1,c2,c3,c4,c5)]:    
            cx.execute("insert into graph values (?,?,?,?,?)", t)
    except:
        pass
        
    cx.commit()
    
def zjm2():
    c1=Button(math2,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    math2.destroy()
    os.system("menu.py")
def draw3():
    aa=jzb.get()
    b=s2.get()
    c=e2.get()
    
    a=arange(eval(s2.get()),eval(e2.get()),0.02)

    p=eval(jzb.get())
    
    plt.subplot(111,polar=True)
    
    plt.plot(a,p,color="red",linewidth=2)
    plt.legend()

    
    name0='%s,%s,%s,3'%(aa,b,c)
    name=''
    for i in name0:
        if i !='*' and i != '/':
            name=name+i
        if i =='*':
            pass
        if i=='/':
            name=name+'~'
 
            
    trace='.\graph\%s.png'%(name)
 
    
    plt.savefig(trace)
    plt.show()
    domain='[%s,%s]'%(b,c)
    
    sql_graph(name0,aa,domain,'polar',trace)
    plt.show()

def draw4():
    x=linspace(eval(s3.get()),eval(e3.get()),1000)
    y=eval(ds1.get())
    plt.subplot(111)
    plt.semilogx(x,y,lw=2)
    plt.ylim(0,1.5)
    plt.xlabel('log(x)')
    plt.ylabel('y')
    
    
    a=ds1.get()
    b=s3.get()
    c=e3.get()
    
    name0='%s,%s,%s,4'%(a,b,c)
    name=''
    for i in name0:
        if i !='*' and i != '/':
            name=name+i
        if i =='*':
            pass
        if i=='/':
            name=name+'~'
            
    trace='.\graph\%s.png'%(name)
 
    
    plt.savefig(trace)
    plt.show()
    domain='[%s,%s]'%(b,c)
    sql_graph(name,a,domain,'logX',trace)

def draw5():
    x=linspace(eval(s3.get()),eval(e3.get()),1000)
    y=eval(ds1.get())
    plt.subplot(111)
    plt.semilogy(x,y,lw=2)
    plt.ylim(0,1.5)
    plt.xlabel('x')
    plt.ylabel('log(y)')
    
    a=ds1.get()
    b=s3.get()
    c=e3.get()
    
    name0='%s,%s,%s,5'%(a,b,c)
    name=''
    for i in name0:
        if i !='*' and i != '/':
            name=name+i
        if i =='*':
            pass
        if i=='/':
            name=name+'~'
            
    trace='.\graph\%s.png'%(name)
 
    
    plt.savefig(trace)
    plt.show()
    domain='[%s,%s]'%(b,c)
    sql_graph(name,a,domain,'logY',trace)
    

def draw6():
    x=linspace(eval(s3.get()),eval(e3.get()),1000)
    y=eval(ds1.get())
    plt.subplot(111)
    plt.loglog(x,y,lw=2)
    plt.ylim(0,1.5)
    plt.xlabel('log(x)')
    plt.ylabel('log(y)')

    a=ds1.get()
    b=s3.get()
    c=e3.get()
    
    name0='%s,%s,%s,6'%(a,b,c)
    name=''
    for i in name0:
        if i !='*' and '#':
            name=name+i
        if i =='*':
            pass
        if i=='/':
            name=name+'~'
            
    trace='.\graph\%s.png'%(name)
 
    
    plt.savefig(trace)
    plt.show()
    domain='[%s,%s]'%(b,c)
    sql_graph(name,a,domain,'logX',trace)
    
math2=Tk()
canvas = Canvas(math2,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
c2=Button(math2,image=im3,command=zjm2).place(x=820,y=600)
canvas.create_image(500,333,image = im)
canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->函数绘图',font=('', 20 ,'bold'),fill='white')
canvas.create_text(500,70,text='(极坐标&对数坐标)',font=('', 20 ,'bold'),fill='white')
canvas.create_text(120,150,text='极坐标图像：',font=('', 20 ,'bold'),fill='white')
canvas.create_text(150,200,text='解析式：P(a)=',font=('', 20 ,'bold'),fill='white')

jzb=Entry(math2,width=20,font=('', 20 ,'bold'),bd=2)
jzb.place(x=280,y=185)
jzb.insert(END,'cos(5*a)')
canvas.create_text(220,250,text='定义域：【     ,     】',font=('', 20 ,'bold'),fill='white')
s2=Entry(math2,width=5,font=('', 15 ,'bold'),bd=2)
s2.insert(END,0)
s2.place(x=195,y=235)

e2=Entry(math2,width=5,font=('', 15 ,'bold'),bd=2)
e2.place(x=285,y=235)
e2.insert(END,2*pi)

b3=Button(math2,width=10,text='绘图',font=('', 20 ,'bold'),bg='lightblue',command=draw3)
b3.place(x=700,y=200)

canvas.create_text(130,300+30,text='对数坐标图像：',font=('', 20 ,'bold'),fill='white')
canvas.create_text(150,200+180,text='解析式：F(x)=',font=('', 20 ,'bold'),fill='white')

ds1=Entry(math2,width=20,font=('', 20 ,'bold'),bd=2)
ds1.place(x=280,y=185+180)
ds1.insert(END,'abs(1/(1+0.1j*x))')

canvas.create_text(220,250+180,text='定义域：【     ,     】',font=('', 20 ,'bold'),fill='white')
s3=Entry(math2,width=5,font=('', 15 ,'bold'),bd=2)
s3.insert(END,0.1)
s3.place(x=195,y=235+180)

e3=Entry(math2,width=5,font=('', 15 ,'bold'),bd=2)
e3.place(x=285,y=235+180)
e3.insert(END,1000)

b4=Button(math2,width=10,text='绘图(X)',font=('', 20 ,'bold'),bg='lightblue',command=draw4)
b4.place(x=50,y=500)

b5=Button(math2,width=10,text='绘图(Y)',font=('', 20 ,'bold'),bg='lightblue',command=draw5)
b5.place(x=300,y=500)

b6=Button(math2,width=10,text='绘图(XY)',font=('', 20 ,'bold'),bg='lightblue',command=draw6)
b6.place(x=550,y=500)


canvas.pack()
mainloop()

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
    
def draw1():
    a=hs.get()
    b=s1.get()
    c=e1.get()
    
    x = linspace(eval(s1.get()), eval(e1.get()), 1000)
    y = eval(hs.get())
    plt.figure(figsize=(8,4))
    plt.plot(x,y,label=hs.get(),color="red",linewidth=2)
    plt.legend()
    

    name0='%s,%s,%s,1'%(a,b,c)
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
    sql_graph(name,a,domain,'Rectangular Plane',trace)

    
def draw2():
    u,v=mgrid[-4:4:30j,-4:4:30j]
    x=eval(x1.get())
    y=eval(y1.get())
    z=eval(z1.get())
    ax=plt.subplot(111,projection='3d')
    ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    a=x1.get()
    b=y1.get()
    c=z1.get()
    name0='%s,%s,%s,1'%(a,b,c)
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
def zjm2():
    c1=Button(math1,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    math1.destroy()
    os.system("menu.py")

math1=Tk()
canvas = Canvas(math1,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
c2=Button(math1,image=im3,command=zjm2).place(x=820,y=600)
canvas.create_image(500,333,image = im)
canvas.create_text(500,20+10,text='基于Python的专业辅助计算系统-->函数绘图',font=('', 25 ,'bold'),fill='white')
canvas.create_text(120,100,text='二维函数图像：',font=('', 20 ,'bold'),fill='white')
canvas.create_text(150,150,text='函数解析式：f(x)=',font=('', 20 ,'bold'),fill='white')

hs=Entry(math1,width=20,font=('', 20 ,'bold'),bd=2)
hs.place(x=280,y=135)
hs.insert(END,'sin(x)')
canvas.create_text(195,200,text='定义域：【     ,     】',font=('', 20 ,'bold'),fill='white')
s1=Entry(math1,width=5,font=('', 15 ,'bold'),bd=2)
s1.insert(END,0)
s1.place(x=175,y=185)

e1=Entry(math1,width=5,font=('', 15 ,'bold'),bd=2)
e1.place(x=265,y=185)
e1.insert(END,10)

b1=Button(math1,width=10,text='绘图',font=('', 20 ,'bold'),bg='lightblue',command=draw1)
b1.place(x=700,y=150)

canvas.create_text(120,280,text='多元函数图像：',font=('', 20 ,'bold'),fill='white')
canvas.create_text(230,330,text='参数方程（可用参数(u,v)）:',font=('', 20 ,'bold'),fill='white')

canvas.create_text(80,380,text='X=',font=('', 20 ,'bold'),fill='white')
canvas.create_text(80,430,text='Y=',font=('', 20 ,'bold'),fill='white')
canvas.create_text(80,480,text='Z=',font=('', 20 ,'bold'),fill='white')

x1=Entry(math1,width=20,font=('', 20 ,'bold'),bd=2)
x1.insert(END,'u')
x1.place(x=110,y=365)

y1=Entry(math1,width=20,font=('', 20 ,'bold'),bd=2)
y1.place(x=110,y=415)
y1.insert(END,'v')

z1=Entry(math1,width=20,font=('', 20 ,'bold'),bd=2)
z1.place(x=110,y=465)
z1.insert(END,'u*exp(-u**2-v**2)')
b2=Button(math1,width=10,text='绘图',font=('', 20 ,'bold'),bg='lightblue',command=draw2)
b2.place(x=700,y=450)

canvas.pack()
mainloop()

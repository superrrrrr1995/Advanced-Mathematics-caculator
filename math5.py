#coding=utf-8
from Tkinter import *
import sqlite3 #导入模块  #
import time
import os
import operator
import time

def zjm2():
    c1=Button(root,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    root.destroy()
    os.system("menu.py")
    
def find():
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    cu.execute("select * from function")   
    res=cu.fetchall()
    for i in range(8):
        t[i].delete(1.0,END)
    for function in res:
        if function[1]==e.get():
            for i in range(8):
                
                t[i].insert(END,function[i]+'\n')
            
t=[0,0,0,0,0,0,0,0,0]
t0=[0,0,0,0,0,0,0,0,0]
c=['函数','解析式','定义域','导函数','不定积分','定积分','零点','泰勒展开']

root=Tk()

canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)


c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)
canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->函数查询',font=('', 20 ,'bold'),fill='white')
canvas.create_text(180,100,text='函数解析式:',font=('', 20 ,'bold'),fill='white')

e=Entry(root,font=('',20),width=35)
e.place(x=280,y=85)
e.insert(END,'x')

for i in range(8):
    t0[i]=Text(root,width=13,height=1,bd=0)
    t0[i].insert(END,c[i]+'\n')
    t0[i].place(x=100+100*i,y=170)
    
    t[i]=Text(root,width=13,height=20,bd=0)
    
    t[i].place(x=100+100*i,y=190)


Button(root,text='查询',command=find,font=('', 15 ,'bold')).place(x=800,y=85)
canvas.pack()
mainloop()

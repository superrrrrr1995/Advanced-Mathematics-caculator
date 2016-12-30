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
    
    if e0.get()=='1':
        cu.execute("select * from dwsy1")
        res=cu.fetchall()
        for i in range(8):
            t0[i].delete(1.0,END)
            
            t0[i].insert(END,dwsy1[i])
                
            t[i].delete(1.0,END)
        
        for data in res:
            if data[0][0:10:1]==e.get():
                for i in range(3):                
                     t[i*2].insert(END,data[i][0:11:1]+'\n'+data[i][11::]+'\n')

                
    if e0.get()=='2':
        cu.execute("select * from dwsy2")
        res=cu.fetchall()
        for i in range(8):
            t0[i].delete(1.0,END)
            t0[i].insert(END,dwsy2[i])
            t[i].delete(1.0,END)
        
        for data in res:
            if data[0][0:10:1]==e.get():
                for i in range(5):                
                     t[i].insert(END,data[i][0:11:1]+'\n'+data[i][11::]+'\n')
      
    if e0.get()=='3':
        cu.execute("select * from dwsy3")
       
        res=cu.fetchall()
        
        for i in range(8):
            t0[i].delete(1.0,END)
            t0[i].insert(END,dwsy3[i])
            t[i].delete(1.0,END)
        
        for data in res:
            if data[0][0:10:1]==e.get():
                for i in range(8):                
                     t[i].insert(END,data[i][0:11:1]+'\n'+data[i][11::]+'\n')
    if e0.get()=='4':
        
        cu.execute("select * from dwsy4")
        res=cu.fetchall()
        
        for i in range(8):
            t0[i].delete(1.0,END)
            t0[i].insert(END,dwsy4[i])
            t[i].delete(1.0,END)
        
        for data in res:
            if data[0][0:10:1]==e.get():
                for i in range(5):                
                     t[i].insert(END,data[i][0:11:1]+'\n'+data[i][11::]+'\n')
     
   
            
t=[0,0,0,0,0,0,0,0,0]
t0=[0,0,0,0,0,0,0,0,0]
dwsy1=['时间','','实验数据','','相对误差','','','']
dwsy2=['时间','静态','静态误差','动态','动态误差','','','']
dwsy3=['时间','光栅常数','紫光波长','紫光误差','黄内光波长','黄内光误差','黄外光波长','黄外光误差']
dwsy4=['时间','Fe模量','不确定度','Cu模量','不确定度','','','']

root=Tk()

canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)


c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)
canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->实验查询',font=('', 20 ,'bold'),fill='white')
canvas.create_text(220,100,text='实验编号:',font=('', 20 ,'bold'),fill='white')
canvas.create_text(430+40,100,text='实验日期:',font=('', 20 ,'bold'),fill='white')
canvas.create_text(500,150,text='1.杨氏拉伸  2.密立根油滴  3.光栅衍射  4.动态杨氏',font=('', 20 ,'bold'),fill='white')

e0=Entry(root,font=('',20),width=5)
e0.place(x=40+270,y=85)
e0.insert(END,'3')


e=Entry(root,font=('',20),width=15)
e.place(x=40+500,y=85)
e.insert(END,'2015-03-29')

for i in range(8):
    t0[i]=Text(root,width=13,height=1,bd=0)
    t0[i].place(x=100+100*i,y=170)
    
    t[i]=Text(root,width=13,height=20,bd=0)
    
    t[i].place(x=100+100*i,y=190)


Button(root,text='查询',command=find,font=('', 15 ,'bold')).place(x=800,y=85)
canvas.pack()
mainloop()

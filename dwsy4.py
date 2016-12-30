# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time
from math import *
import sqlite3
def sql_dwsy4(a0,a1,a2,a3,a4,a5,a6,a7,a8):
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table dwsy4( 时间 varchar(10) primary key,杨氏模量FeE11 varchar(10),Fe不确定度 varchar(10),杨氏模量CuE11 varchar(10),Cu不确定度 varchar(10),Fe直径mm varchar(10),Cu直径mm varchar(10), Fe频率Hz varchar(10), Cu频率Hz varchar(10) )""")
    except:
        pass
    try:
        for t in[(a0,a1,a2,a3,a4,a5,a6,a7,a8)]:    
            cx.execute("insert into dwsy4 values (?,?,?,?,?,?,?,?,?)", t)
    except:
        pass
    cx.commit()
def zjm2():
    c1=Button(dwsy4,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    dwsy4.destroy()
    os.system("menu.py")
    
def qcsj():    
    for i in range(6):
        f1[i].delete(0,END)
        f2[i].delete(0,END)
        c1[i].delete(0,END)
        c2[i].delete(0,END)
    for i in range(2):
        l[i].delete(0,END)
        m[i].delete(0,END)
def scbg():
    dwsy41=Toplevel()
    canvas = Canvas(dwsy41,width = 1000, height = 666)
    im=PhotoImage(file='dwsy41.gif')
    canvas.create_image(500,333,image = im)
    f11=[];f21=[];c11=[];c21=[]
    for i in range(6):
        f11.append(eval(f1[i].get()))
        f21.append(eval(f2[i].get()))
        c11.append(eval(c1[i].get()))
        c21.append(eval(c2[i].get()))
    pjs=[];ud=[0,0,0,0]
    pjs.append(sum(f11)/6.0)
    pjs.append(sum(f21)/6.0)
    pjs.append(sum(c11)/6.0)
    pjs.append(sum(c21)/6.0)
    bzc1=0;bzc2=0;bzc3=0;bzc4=0
    for i in range(6):
        bzc1=bzc1+(f11[i]-pjs[0])**2
        bzc2=bzc2+(f21[i]-pjs[1])**2
        bzc3=bzc3+(c11[i]-pjs[2])**2
        bzc4=bzc4+(c21[i]-pjs[3])**2
    bzc=[bzc1,bzc2,bzc3,bzc4]
    for i in range(4):
        ud[i]=sqrt((bzc[i]/sqrt(5)*1.11)**2+(0.683*0.004)**2)
    bzc=[sqrt(bzc1/6.0),sqrt(bzc2/6.0),sqrt(bzc3/6.0),sqrt(bzc4/6.0)]
    res=[]
    
    for i in range(2):
        canvas.create_text(335+20*i,75+160*i,text='%.3f'%(pjs[i]),fill='blue',font=('', 10, 'bold'))
        canvas.create_text(780,65+170*i,text='%.3f'%(bzc[i]),fill='blue',font=('', 10, 'bold'))
 
        canvas.create_text(520+15*i,130+160*i,text='%.3f'%(ud[i]),fill='blue',font=('', 10, 'bold'))
        canvas.create_text(630,130+160*i,text='%.3f'%(pjs[i]),fill='blue',font=('', 10, 'bold'))
        canvas.create_text(700,130+160*i,text='%.3f'%(ud[i]),fill='blue',font=('', 10, 'bold'))
        
        e=1.6067*(eval(l[i].get())**3)*eval(m[i].get())/(pjs[2*i]**4)*(pjs[2*i+1])**2*1e-8
        u=sqrt((3*0.0014/eval(l[i].get()))**2+(0.14/eval(m[i].get()))**2+(4*0.003/pjs[i])**2+(2*0.15/pjs[i+1]))
       
        canvas.create_text(505,360+180*i,text='%.3f'%(e),fill='blue',font=('', 10, 'bold'))
        
        canvas.create_text(480,430+180*i,text='%.3f'%(u),fill='blue',font=('', 10, 'bold'))
        canvas.create_text(655,430+180*i,text='%.3f'%(e),fill='blue',font=('', 10, 'bold'))
        canvas.create_text(735,430+180*i,text='%.3f'%(u),fill='blue',font=('', 10, 'bold'))
        res.append(e)
        res.append(u)
   
    
    canvas.create_text(630,175,text=l[0].get(),fill='blue',font=('', 10, 'bold'))
    canvas.create_text(630,205,text=m[0].get(),fill='blue',font=('', 10, 'bold'))
    canvas.create_text(200,495,text='%.3f'%(pjs[2]),fill='blue',font=('', 10, 'bold'))
    canvas.create_text(270,495,text='%.3f'%(bzc[2]),fill='blue',font=('', 10, 'bold'))
    canvas.create_text(410,495,text=l[1].get(),fill='blue',font=('', 10, 'bold'))
    canvas.create_text(620,495,text=m[1].get(),fill='blue',font=('', 10, 'bold'))
    
    canvas.create_text(190,540,text='%.2f'%(pjs[3]),fill='blue',font=('', 10, 'bold'))
    canvas.create_text(260,540,text='%.2f'%(bzc[3]),fill='blue',font=('', 10, 'bold'))

    canvas.pack()
    time0=str(time.strftime('%Y-%m-%d %H:%M:%S')) 
    sql_dwsy4(time0,res[0],res[1],res[2],res[3],str(f11),str(c11),str(f21),str(c21))
    mainloop()


f10=[5.980,5.970,5.968,5.968,5.969,5.975]
c10=[6.092,6.100,6.090,6.085,6.088,6.090]
f20=[1176.0,1176.1,1176.2,1176.1,1176.2,1176.2]
c20=[863.7,863.9,863.9,863.8,863.8,864.0]
l0=[14.970,14.976]
m0=[32.45,36.18]


dwsy4 = Tk()
canvas = Canvas(dwsy4,width = 1000, height = 666)
im=PhotoImage(file='dwsy4.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image = im)
c2=Button(dwsy4,image=im3,command=zjm2).place(x=820,y=600)
f1=[];c1=[];f2=[];c2=[];l=[0,0];m=[0,0]

for i in range(6):
    f1.append(1);f2.append(1);c1.append(1);c2.append(1)
    f1[i]=Entry(dwsy4,width=8)
    f1[i].insert(END,f10[i])
    f1[i].place(x=230+80*i,y=260)
    c1[i]=Entry(dwsy4,width=8)
    c1[i].insert(END,c10[i])
    c1[i].place(x=230+80*i,y=310)

    f2[i]=Entry(dwsy4,width=9)
    f2[i].insert(END,f20[i])
    f2[i].place(x=230+92*i,y=455)
    c2[i]=Entry(dwsy4,width=9)
    c2[i].insert(END,c20[i])
    c2[i].place(x=230+92*i,y=490)
for i in range(2):
    l[i]=Entry(dwsy4,width=8)
    l[i].insert(END,l0[i])
    l[i].place(x=710,y=260+50*i)
    m[i]=Entry(dwsy4,width=8)
    m[i].insert(END,m0[i])
    m[i].place(x=790,y=260+50*i)
 

Button(dwsy4,width=10,height=1,text='生成实验报告',fg='red',command=scbg).place(x=350,y=610)
Button(dwsy4,width=10,height=1,text='清楚所有数据',fg='red',command=qcsj).place(x=550,y=610)
canvas.pack()
mainloop()

# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time
from math import *
import sqlite3
def sql_dwsy2(a0,a1,a2,a3,a4,a5,a6,a7,a8):
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table dwsy2( 时间 varchar(10) primary key,静态 varchar(10),静态误差 varchar(10),动态 varchar(10),动态误差 varchar(10), U平衡V varchar(10),时间tg varchar(10),U上升 varchar(10),时间t1 varchar(10)  )""")
    except:
        pass
     
    try:
        for t in[(a0,a1,a2,a3,a4,a5,a6,a7,a8)]:    
            cx.execute("insert into dwsy2 values (?,?,?,?,?,?,?,?,?)", t)
    except:
        pass
    cx.commit()
def zjm2():
    c1=Button(dwsy2,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    dwsy2.destroy()
    os.system("menu.py")
def qcsj():    
    for i in range(6):
        u1[i].delete(0,END)
        u2[i].delete(0,END)
        tg[i].delete(0,END)
        t1[i].delete(0,END)
    for i in range(32):
        canvas.delete(a[i])
def scbg():
    try:
        for i in range(32):
            canvas.delete(a[i])
    except:
        pass
    u11=[];tg1=[];u21=[];t11=[]
    for i in range(6):
        u11.append(eval(u1[i].get()))
        u21.append(eval(u2[i].get()))
        tg1.append(eval(tg[i].get()))
        t11.append(eval(t1[i].get()))
    pjs=[]
    pjs.append(sum(u11)/6.0)
    pjs.append(sum(tg1)/6.0)
    pjs.append(sum(u21)/6.0)
    pjs.append(sum(t11)/6.0)
    bzc1=0;bzc2=0;bzc3=0;bzc4=0
    for i in range(6):
        bzc1=bzc1+(u11[i]-pjs[0])**2
        bzc2=bzc2+(tg1[i]-pjs[1])**2
        bzc3=bzc3+(u21[i]-pjs[2])**2
        bzc4=bzc4+(t11[i]-pjs[3])**2
    bzc=[sqrt(bzc1/6.0),sqrt(bzc2/6.0),sqrt(bzc3/6.0),sqrt(bzc4/6.0)]
    for i in range(4): 
        a[i]=canvas.create_text(570+3,140+35*i,text='%.2f'%(pjs[i]),fill='blue',font=('', 10, 'bold'))
        a[i+4]=canvas.create_text(570+48+3,140+35*i,text='%.3f'%(bzc[i]),fill='blue',font=('', 10, 'bold'))
        
    a[8]=canvas.create_text(325,310,text='%.2f'%(pjs[0]),fill='blue',font=('', 10, 'bold'))
    a[9]=canvas.create_text(780,310,text='%.3f'%(bzc[0]/sqrt(5)),fill='blue',font=('', 10, 'bold'))
    
    a[10]=canvas.create_text(335,350,text='%.3f'%(1.11*bzc[0]/sqrt(5)),fill='blue',font=('', 10, 'bold'))
    a[11]=canvas.create_text(490,350,text='%.2f'%(pjs[0]),fill='blue',font=('', 10, 'bold'))
    a[12]=canvas.create_text(570,350,text='%.3f'%(1.11*bzc[0]/sqrt(5)),fill='blue',font=('', 10, 'bold'))

    a[13]=canvas.create_text(255,395,text='%.2f'%(pjs[1]),fill='blue',font=('', 10, 'bold'))
    a[14]=canvas.create_text(405,395,text='%.2f'%(pjs[2]),fill='blue',font=('', 10, 'bold'))
    a[15]=canvas.create_text(525,395,text='%.2f'%(pjs[3]),fill='blue',font=('', 10, 'bold'))

    q1=(1.43e5)/((pjs[1]*(1+0.02*sqrt(pjs[1])))**1.5)/pjs[0]

    a[16]=canvas.create_text(660,435,text='%.3f'%(q1),fill='blue',font=('', 10, 'bold'))
    n1=int(q1/1.602+0.5)
    a[17]=canvas.create_text(250,505,text='%.0f'%(n1),fill='blue',font=('', 10, 'bold'))
    e1=q1/n1
    a[18]=canvas.create_text(445,505,text='%.3f'%(e1),fill='blue',font=('', 10, 'bold'))
    wc1=fabs(e1-1.602)/1.602*100
    a[19]=canvas.create_text(730,505,text='%.3f'%(wc1),fill='blue',font=('', 10, 'bold'))

    q2=1.429e5*(1/pjs[1]+1/pjs[3])*(1/pjs[1])**0.5*(1/pjs[2])*(1/(1+0.01958*sqrt(pjs[1])))**1.5
    a[20]=canvas.create_text(730,550,text='%.3f'%(q2),fill='blue',font=('', 10, 'bold'))
    n2=int(q2/1.602+0.5)
    a[21]=canvas.create_text(250,595,text='%.0f'%(n2),fill='blue',font=('', 10, 'bold'))
    e2=q2/n2
    a[22]=canvas.create_text(445,595,text='%.3f'%(e2),fill='blue',font=('', 10, 'bold'))
    wc2=fabs(e2-1.602)/1.602*100
    a[23]=canvas.create_text(730,595,text='%.3f'%(wc2),fill='blue',font=('', 10, 'bold'))
    
    syjg=[q1,q1/1.602,e1,wc1,q2,q2/1.602,e2,wc2]
    
        
    for i in range(4):
        a[24+i]=canvas.create_text(668+48*i,165,text='%.3f'%(syjg[i]),fill='blue',font=('', 10, 'bold'))
        a[28+i]=canvas.create_text(668+48*i,165+70,text='%.3f'%(syjg[i+4]),fill='blue',font=('', 10, 'bold'))    
    canvas.pack()


  

    time0=str(time.strftime('%Y-%m-%d %H:%M:%S')) 
    sql_dwsy2(time0,e1,wc1,e2,wc2,str(u11),str(tg1),str(u21),str(t11))
    mainloop()


u10=[166,166,166,167,167,167,167]
tg0=[25.5,24.7,24.8,24.6,24.9,25.3]
u20=[410,410,409,410,410,409]
t10=[16.3,16.3,16.4,16.5,16.1,16.1]

if __name__ == '__main__':
    global dwsy2,a
    a=[0 for x in range(32)]
    dwsy2 = Tk()
    canvas = Canvas(dwsy2,width = 1000, height = 666)
    im=PhotoImage(file='dwsy2.gif')
    im3=PhotoImage(file='3.gif')
    canvas.create_image(500,333,image = im)
    c2=Button(dwsy2,image=im3,command=zjm2).place(x=820,y=600)
    u1=[];tg=[];u2=[];t1=[]
    for i in range(6):
        u1.append(1);tg.append(1);u2.append(1);t1.append(1)
        u1[i]=Entry(dwsy2,width=5)
        u1[i].insert(END,u10[i])
        u1[i].place(x=265+48*i,y=130)
    
        tg[i]=Entry(dwsy2,width=5)
        tg[i].insert(END,tg0[i])
        tg[i].place(x=265+48*i,y=165)
    
        u2[i]=Entry(dwsy2,width=5)
        u2[i].insert(END,u20[i])
        u2[i].place(x=265+48*i,y=200)
    
        t1[i]=Entry(dwsy2,width=5)
        t1[i].insert(END,t10[i])
        t1[i].place(x=265+48*i,y=235)

    Button(dwsy2,width=10,height=1,text='生成实验报告',fg='red',command=scbg).place(x=350,y=610)
    Button(dwsy2,width=10,height=1,text='清楚所有数据',fg='red',command=qcsj).place(x=550,y=610)
    canvas.pack()
    mainloop()

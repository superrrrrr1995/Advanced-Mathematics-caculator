# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time
from math import *
import sqlite3
def sql_dwsy2(a0,a1,a2,a3,a4,a5,a6,a7):
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table dwsy3( 时间 varchar(10) primary key,光栅常数 varchar(10),紫光波长 varchar(10),紫光误差 varchar(10),黄内光波长 varchar(10), 黄内光误差 varchar(10),黄外光波长 varchar(10),黄外光误差 varchar(10)  )""")
    except:
        pass
     
    try:
        for t in[(a0,a1,a2,a3,a4,a5,a6,a7)]:    
            cx.execute("insert into dwsy3 values (?,?,?,?,?,?,?,?)", t)
    except:
        pass
    cx.commit()
    
def zjm2():
    c1=Button(dwsy3,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    dwsy3.destroy()
    os.system("menu.py")
    
def plus(x,y):
    a1=int(x)
    b1=int(x*100)-a1*100
    c1=int(x*10000)-a1*10000-b1*100
    a2=int(y)
    b2=int(y*100)-a2*100
    c2=int(y*10000)-a2*10000-b2*100
    a=a1+a2
    b=b1+b2
    c=c1+c2
    if c>60:
        c=c-60
        b=b+1
    if b>60:
        b=b-60
        a=a+1
    if c==39:
        c=0
        
        
    return a+0.01*b+0.0001*c
def minus(x,y):
    if x<y:x,y=y,x
    a1=int(x)
    b1=int(x*100)-a1*100
    c1=int(x*10000)-a1*10000-b1*100
    a2=int(y)
    b2=int(y*100)-a2*100
    c2=int(y*10000)-a2*10000-b2*100
    a=a1-a2
    b=b1-b2
    c=c1-c2
    if c<0:
        c=c+60
        b=b-1
    if b<0:
        b=b+60
        a=a-1
    if c==99:
        c=0
        b=b+1
    return a+0.01*b+0.0001*c

def divide(x,q):
    a1=int(x)
    b1=int(x*100)-a1*100
    c1=int(x*10000)-a1*10000-b1*100
    if c1==99:
        b1=b1+1
        c1=0
    a=a1/q
    b=b1/q
    c=c1/q
    q1=a1%q
    q2=b1%q
    if q1!=0:
        b=b+q1*(60/q)
    if q2!=0:
        c=c+q2*(60/q)
    return a+0.01*b+0.0001*c
def zh(x):
    a1=int(x)
    b1=int(x*100)-a1*100
    c1=int(x*10000)-a1*10000-b1*100
    return a1+b1/0.6*0.01+c1/0.6*0.0001

def ff(x1,y1,x2,y2):
    a0=minus(eval(x1),eval(x2))
    b0=minus(eval(y1),eval(y2))
    m=plus(a0,b0)
    return divide(m,4)

def scbg():
    dwsy31=Toplevel()
    canvas = Canvas(dwsy31,width = 1000, height = 726)
    im=PhotoImage(file='dwsy31.gif')
    canvas.create_image(500,333,image = im)    
    ff1=[]
    s=0
    for i in range(6):
        m=ff(f1[i].get(),f2[i].get(),f3[i].get(),f4[i].get())
        ff1.append(m)
        s=plus(s,m)
        if i==0:
            canvas.create_text(450,70,text='%.4f'%(ff1[i]),font=('' ,10,'bold'),fill='blue')
        else:
            canvas.create_text(310-125+125*i,90,text='%.4f'%(ff1[i]),font=('' ,10,'bold'),fill='blue')
    pjs=divide(s,6)
    canvas.create_text(330,125,text='%.4f'%(pjs),font=('' ,10,'bold'),fill='blue')
    s=0
    for i in range(6):
        s=s+(ff1[i]-pjs)**2
    bzc=sqrt(s/30.0)
    canvas.create_text(630,125,text='%.4f'%(bzc),font=('' ,10,'bold'),fill='blue')
    s1=1.11*bzc
    canvas.create_text(430,155,text='%.4f'%(s1),font=('' ,10,'bold'),fill='blue')
    u1=sqrt(s1**2+(0.0002*0.683)**2)
    canvas.create_text(820,155,text='%.4f'%(u1),font=('' ,10,'bold'),fill='blue')
    canvas.create_text(270,190,text='%.4f'%(pjs),font=('' ,10,'bold'),fill='blue')
    canvas.create_text(350,190,text='%.4f'%(u1),font=('' ,10,'bold'),fill='blue')
    e1=u1/pjs*100
    canvas.create_text(570,190,text='%.4f'%(e1),font=('' ,10,'bold'),fill='blue')
    pjs=zh(pjs)
    d=546.1/sin(pjs/180*pi)
    canvas.create_text(470,250,text='%.2f'%(d),font=('' ,10,'bold'),fill='blue')
    ud=546.1*cos(pjs/180*pi)*u1/sin(pjs/180*pi)/sin(pjs/180*pi)
    canvas.create_text(690,250,text='%.2f'%(ud),font=('' ,10,'bold'),fill='blue')
    canvas.create_text(360,305,text='%.2f'%(d),font=('' ,10,'bold'),fill='blue')
    canvas.create_text(440,305,text='%.2f'%(ud),font=('' ,10,'bold'),fill='blue')
    e2=ud/d*100
    canvas.create_text(680,305,text='%.2f'%(e2),font=('' ,10,'bold'),fill='blue')
    canvas.create_text(720,305,text='%',font=('' ,20,'bold'),fill='red')
    canvas.create_text(600,570,text='5',font=('' ,15,'bold'),fill='red')
    canvas.create_text(550,570,text='5',font=('' ,15,'bold'),fill='red')
    
    f21=[];bz=[435.8,577.0,579.1]
    m=[]
    for i in range(3):
        m1=ff(g1[4*i].get(),g1[4*i+1].get(),g1[4*i+2].get(),g1[4*i+3].get())
        m2=ff(g2[4*i].get(),g2[4*i+1].get(),g2[4*i+2].get(),g2[4*i+3].get())
        m3=ff(g3[4*i].get(),g3[4*i+1].get(),g3[4*i+2].get(),g3[4*i+3].get())
        pjs1=plus(plus(m1,m2),m3)
        pjs1=divide(pjs1,3)
        
        canvas.create_text(250,375+45*i,text='%.4f'%(m1),font=('' ,10,'bold'),fill='blue')
        canvas.create_text(380,375+45*i,text='%.4f'%(m2),font=('' ,10,'bold'),fill='blue')
        canvas.create_text(500,375+45*i,text='%.4f'%(m3),font=('' ,10,'bold'),fill='blue')
        canvas.create_text(770,375+45*i,text='%.4f'%(pjs1),font=('' ,10,'bold'),fill='blue')
        pjs1=zh(pjs1)
        bc=sin(pjs1/180*pi)/sin(pjs/180*pi)*546.1
        m.append(bc)
        canvas.create_text(495+135*i,520,text='%.2f'%(bc),font=('' ,10,'bold'),fill='blue')
        e=fabs(bc-bz[i])/bz[i]*100
        m.append(e)
        if i<2:
            canvas.create_text(335+330*i,565,text='%.2f'%(e),font=('' ,10,'bold'),fill='blue')
        else:
            canvas.create_text(335,592,text='%.2f'%(e),font=('' ,10,'bold'),fill='blue')
        
    canvas.pack()

    time0=str(time.strftime('%Y-%m-%d %H:%M:%S')) 
    sql_dwsy2(time0,e2,m[0],m[1],m[2],m[3],m[4],m[5])
    
    mainloop()    

    
def qcsj():
    for i in range(6):
        f1[i].delete(0,END)
        f2[i].delete(0,END)
        f3[i].delete(0,END)
        f4[i].delete(0,END)
    for i in range(12):
        g1[i].delete(0,END)
        g2[i].delete(0,END)
        g3[i].delete(0,END)

dwsy3 = Tk()
canvas = Canvas(dwsy3,width = 1000, height = 666)
im=PhotoImage(file='dwsy3.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image = im)
c2=Button(dwsy3,image=im3,command=zjm2).place(x=820,y=600)
Button(dwsy3,width=10,height=1,text='生成实验报告',fg='red',command=scbg).place(x=350,y=610)
Button(dwsy3,width=10,height=1,text='清楚所有数据',fg='red',command=qcsj).place(x=550,y=610)
f10=[33.40,33.40,33.39,33.40,33.40,33.41]
f20=[213.40,213.40,213.40,213.39,213.39,213.39]
f30=[14.50,14.50,14.50,14.51,14.51,14.50]
f40=[194.49,194.50,194.49,194.51,194.51,194.51,194.50]

g10=[31.45,211.45,16.45,196.44,34.12,214.12,14.18,194.18,34.14,214.14,14.16,194.15]
g20=[31.45,211.45,16.45,196.45,34.12,214.12,14.18,194.18,34.14,214.14,14.16,194.16]
g30=[31.45,211.45,16.45,196.45,34.12,214.12,14.18,194.18,34.15,214.15,14.15,194.15]

f1=[0 for i in range(6)]
f2=[0 for i in range(6)]
f3=[0 for i in range(6)]
f4=[0 for i in range(6)]

g1=[0 for i in range(12)]
g2=[0 for i in range(12)]
g3=[0 for i in range(12)]

for i in range(6):
    f1[i]=Entry(dwsy3,width=20)
    f1[i].place(x=232,y=163+35*i)
    f1[i].insert(END,f10[i])
    f2[i]=Entry(dwsy3,width=20)
    f2[i].place(x=389,y=163+35*i)
    f2[i].insert(END,f20[i])
    f3[i]=Entry(dwsy3,width=20)
    f3[i].place(x=389+157,y=163+35*i)
    f3[i].insert(END,f30[i])
    f4[i]=Entry(dwsy3,width=20)
    f4[i].place(x=389+157*2,y=163+35*i)
    f4[i].insert(END,f40[i])
for i in range(12):
    g1[i]=Entry(dwsy3,width=6)
    g1[i].place(x=185+56*i,y=490)
    g1[i].insert(END,g10[i])
    g2[i]=Entry(dwsy3,width=6)
    g2[i].place(x=185+56*i,y=530)
    g2[i].insert(END,g20[i])
    g3[i]=Entry(dwsy3,width=6)
    g3[i].place(x=185+56*i,y=570)
    g3[i].insert(END,g30[i])




canvas.pack()
mainloop()

    

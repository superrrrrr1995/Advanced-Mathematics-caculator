# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time
from math import *
import sqlite3
def sql_dwsy1(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9):
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table dwsy1( 时间 varchar(10) primary key,实验结果E11 varchar(10),误差 varchar(10),X减cm varchar(10),X增cm varchar(10), 钢丝直径mm varchar(10),初读数mm varchar(10),镜尺距cm varchar(10),钢丝长度cm varchar(10) ,光杠杆常数cm varchar(10) )""")
    except:
        print 'error'
    try:
        for t in[(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)]:    
            cx.execute("insert into dwsy1 values (?,?,?,?,?,?,?,?,?,?)", t)
    except:
        pass
    cx.commit()
def zjm2():
    c1=Button(dwsy1,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    dwsy1.destroy()
    os.system("menu.py")

def sybg1():
    global dwsy11,cx,pjz,ud,u
    dwsy11=Toplevel()
    canvas = Canvas(dwsy11,width = 1000, height = 726)
    im=PhotoImage(file='dwsy11.gif')
    canvas.create_image(500,333,image = im)
    s=0
    z=[]
    d2=[]
    for i in range(0,12,1):
        z.append(eval(w1[i].get())/2.0+eval(w2[i].get())/2.0)
        canvas.create_text(295+45*i,75,text=w1[i].get(),fill='orange',font=('', 10,'bold'))
        canvas.create_text(295+45*i,110,text=w2[i].get(),fill='orange',font=('', 10,'bold'))

        canvas.create_text(295+45*i,155,text='%.3f'%(z[i]),fill='orange',font=('', 10,'bold'))        
    m=[]
    for i in range(0,6,1):
        m.append('%.2f'%(z[i+6]-z[i]))
        s=s+eval(m[i])
        canvas.create_text(265+95*i,222,text=m[i],fill='orange',font=('', 10,'bold'))
    pjz='%.4f'%(s/6.0)
    
    canvas.create_text(310,255,text=pjz,fill='orange',font=('', 10,'bold'))
    s1=0
    
    for i in range(6):
        s1=(eval(m[i])-eval(pjz))**2+s1
        
    bzc='%.4f'%(sqrt(s1)/5)
    
    canvas.create_text(535,250,text=bzc,fill='orange',font=('', 10,'bold'))
    
    u='%.4f'%(sqrt((1.11*eval(bzc)/sqrt(6))**2+(0.683*0.05)**2))
    
    canvas.create_text(760,320,text=u,fill='orange',font=('', 10,'bold'))
    canvas.create_text(305,380,text=pjz,fill='orange',font=('', 10,'bold'))
    canvas.create_text(370,380,text=u,fill='orange',font=('', 10,'bold'))
    canvas.create_text(305,410,text=wD.get(),fill='orange',font=('', 10,'bold'))
    canvas.create_text(335,460,text=wD.get(),fill='orange',font=('', 10,'bold'))
    canvas.create_text(335,480,text=wl1.get(),fill='orange',font=('', 10,'bold'))
    canvas.create_text(400,480,text=wl2.get(),fill='orange',font=('', 10,'bold'))
    canvas.create_text(465,480,text=eval(wl1.get())-eval(wl2.get()),fill='orange',font=('', 10,'bold'))
    canvas.create_text(385,500,text=eval(wl1.get())-eval(wl2.get()),fill='orange',font=('', 10,'bold'))
    s2=0
    for i in range(0,6,1):
        s2=s2+(eval(wd[i].get())-sum(d1)/6)**2
        d2.append(eval(wd[i].get())-eval(wd0.get()))
        canvas.create_text(292+70*i,585,text=d2[i],fill='orange',font=('', 10,'bold'))    
    bzc1=sqrt(s2)/5
    ud=sqrt((1.11)*bzc1/sqrt(6)**2+(0.683*0.004)**2)
    cx=sum(d2)/6
    canvas.create_text(292+70*6,585,text='%.4f'%(cx),fill='orange',font=('', 10,'bold'))
    canvas.create_text(292+70*7,585,text='%.4f'%(bzc1),fill='orange',font=('', 10,'bold'))
    canvas.create_text(733,635,text='%.4f'%(ud),fill='orange',font=('', 10,'bold'))
    
    canvas.create_text(275,680,text='%.4f'%(cx),fill='orange',font=('', 10,'bold'))
    canvas.create_text(340,680,text='%.4f'%(ud),fill='orange',font=('', 10,'bold'))
    Button(dwsy11,text='下一页',font=('', 12,'bold'),fg='red',command=sybg2).place(x=800,y=640)
    canvas.pack()
    mainloop()
    
def sybg2():
    dwsy11.destroy()
    dwsy12=Toplevel()
    canvas = Canvas(dwsy12,width = 1000, height = 726)
    
    im=PhotoImage(file='dwsy12.gif')
    canvas.create_image(500,333,image = im)
    
    canvas.create_text(340,75,text=wb.get(),fill='orange',font=('', 10,'bold'))
    canvas.create_text(350,150,text=wb.get(),fill='orange',font=('', 10,'bold'))
    f=6*1.5*9.8
    canvas.create_text(360,215,text=f,fill='orange',font=('', 10,'bold'))
    y=8*f*eval(wD.get())*(eval(wl1.get())-eval(wl2.get()))/pi/cx/cx/eval(wb.get())/eval(pjz)*1e-5
    canvas.create_text(350,270,text='%.4f'%(y),fill='orange',font=('', 10,'bold'))
    ey=sqrt((0.04/(eval(wl1.get())-eval(wl2.get())))**2+(0.3/eval(wD.get()))**2+4*(ud/cx)**2+(0.001/eval(wb.get()))**2+(eval(u)/eval(pjz))**2)
    canvas.create_text(610,330,text='%.4f'%(ey),fill='orange',font=('', 10,'bold'))
    canvas.create_text(345,395,text='%.4f'%(y*ey),fill='orange',font=('', 10,'bold'))
    canvas.create_text(345,420,text='%.4f'%(y),fill='orange',font=('', 10,'bold'))
    canvas.create_text(415,420,text='%.4f'%(ey),fill='orange',font=('', 10,'bold'))
    canvas.create_text(400,535,text='%.4f'%(y),fill='orange',font=('', 10,'bold'))
    canvas.create_text(470,535,text='%.4f'%(ey),fill='orange',font=('', 10,'bold'))
    if 1.9<y-ey and y+ey<2.1:
        canvas.create_text(500,605,text='您的实验很成功喔！',fill='green',font=('', 30,'bold'))
    else:
        canvas.create_text(500,605,text='您的实验有误差喔！',fill='green',font=('', 30,'bold'))
        
    canvas.pack()
    

       
    sx=''
    sy=''
    sd1=''
    for i in range(12):
        aa=w1[i].get()+','
        bb=w2[i].get()+','
        sx=sx+aa
        sy=sy+bb
    for i in range(6):
        sd1=sd1+wd[i].get()+','
    sd0=wd0.get()
    sd=wD.get()
    sl=wl3.get()
    sb=wb.get()
    time0=str(time.strftime('%Y-%m-%d %H:%M:%S')) 
    sql_dwsy1(time0,y,ey,sx,sy,sd1,sd0,sd,sl,sb)

    mainloop()
def qcsj():    
    for i in range(12):
        w1[i].delete(0,END)
        w2[i].delete(0,END)
    for i in range(6):
        wd[i].delete(0,END)
    wD.delete(0,END)
    wl1.delete(0,END)
    wl2.delete(0,END)
    wl3.delete(0,END)
    wd0.delete(0,END)
    wb.delete(0,END)
    

    
    
x=[0.50,0.76,1.00,1.23,1.49,1.72,1.99,2.21,2.46,2.70,2.92,3.18]
y=[0.51,0.76,1.01,1.23,1.50,1.73,2.00,2.22,2.48,2.71,2.95,3.18]
d1=[0.829,0.828,0.828,0.829,0.829,0.828]
d=83.40*2
l=40.30
b=8.330
d0=-0.002




dwsy1 = Tk()


im=PhotoImage(file='dwsy1.gif')
im3=PhotoImage(file='3.gif')
im0=PhotoImage(file='dwsy10.gif')
canvas=Canvas(dwsy1,width = 1000, height = 666)
canvas.create_image(500,333,image = im)
c2=Button(dwsy1,image=im3,command=zjm2).place(x=820,y=600)
w1=[]
w2=[]
for i in range(12):
    w1.append(1)
    w1[i]=Entry(dwsy1,width=4,text=x[i])
    w1[i].place(x=279+45*i,y=160)    
    w1[i].insert(END,x[i])

for i in range(12):
    w2.append(1)
    w2[i]=Entry(dwsy1,width=4)
    w2[i].place(x=279+45*i,y=195)    
    w2[i].insert(END,y[i])
    
wD=Entry(dwsy1,width=12)
wD.place(x=320,y=230)
wD.insert(END,d)

wl1=Entry(dwsy1,width=25)
wl1.place(x=205,y=365)
wl1.insert(END,50.3)

wl2=Entry(dwsy1,width=25)
wl2.place(x=410,y=365)
wl2.insert(END,10.3)

wl3=Entry(dwsy1,width=25)
wl3.place(x=615,y=365)
wl3.insert(END,40.3)

wd0=Entry(dwsy1,width=10)
wd0.place(x=485,y=410)
wd0.insert(END,d0)

wd=[]
for i in range(6):
    wd.append(1)
    wd[i]=Entry(dwsy1,width=10)
    wd[i].place(x=285+90*i,y=495)
    wd[i].insert(END,d1[i])
    
wb=Entry(dwsy1,width=10)
wb.place(x=355,y=535)
wb.insert(END,b)

Button(dwsy1,width=10,height=2,text='生成实验报告',fg='red',command=sybg1).place(x=350,y=600)
Button(dwsy1,width=10,height=2,text='清楚所有数据',fg='red',command=qcsj).place(x=550,y=600)
canvas.pack()


mainloop()




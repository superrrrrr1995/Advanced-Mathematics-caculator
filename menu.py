# -*- coding:utf-8 -*-
from imp import reload
from Tkinter import *
import time
import os
def a2():#后退小车左移动
    c1=Button(root,image=im3)
    c1.update()
    for a in range(900,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    root.destroy()
def a20():
    a2()
    os.system("menu.py")    
def a1(m,x1,y1):#小车右移动
    c=Button(root,image=im2)
    c.update()
    for a in range(x1,y1):        
        c.place(x=a,y=100*m)
        c.update()
        time.sleep(0.0001)
    canvas.delete(xt,d[0],d[1],d[2],d[3],d[4])
    c2.config(command=a20)
def dwsy1():
    a1(1,50,1000)
    root.destroy()
    os.system("dwsy10.py")
def dwsy2():
    a1(2,50,1000)
    root.destroy()
    os.system("dwsy20.py")
def dwsy3():
    a1(3,50,1000)
    root.destroy()
    os.system("dwsy30.py")
def dwsy4():
    a1(4,50,1000)
    root.destroy()
    os.system("dwsy40.py")
def dwsy5():
    a1(5,50,1000)
    root.destroy()
    os.system("dwsy5.py")
def math1():
    a1(1,50,1000)
    root.destroy()
    os.system("math1.py")
def math2():
    a1(2,50,1000)
    root.destroy()
    os.system("math2.py")
def math3():
    a1(3,50,1000)
    root.destroy()
    os.system("math3.py")
def math4():
    a1(4,50,1000)
    root.destroy()
    os.system("math4.py")
def math5():
    a1(5,50,1000)
    root.destroy()
    os.system("math5.py")
def tl1():
    a1(1,50,1000)
    root.destroy()
    os.system("hungary.py")
def tl2():
    a1(2,50,1000)
    root.destroy()
    os.system("kruscal.py")
def tl3():
    a1(3,50,1000)
    root.destroy()
    os.system("tarjan.py")
def tl4():
    a1(4,50,1000)
    root.destroy()
    os.system("zdlj.py")
def tl5():
    pass

def data1():
    a1(1,50,1000)
    root.destroy()
    os.system("fitting.py")
def data2():
    a1(2,50,1000)
    root.destroy()
    os.system("pca.py")
def data3():
    a1(3,50,1000)
    root.destroy()
    os.system("kmeans.py")
def data4():
    pass
def data5():
    pass

def b1():  #进入科学计算器
    a1(1,50,1000)
    root.destroy()
    os.system("kxjsq.py")
def b2():#进入高数&现代
    a1(2,50,1000)
    d2=canvas.create_text(500,50,text='基于Python的专业辅助计算系统-->高等数学&线性代数',fill='white',font=('', 20,'bold'))
    a=['绘图(直角坐标)','绘图（对数坐标&极坐标）','微积分计算','线性代数','函数查询']
    for i in range(5):
        d[i]=canvas.create_text(500,150+100*i,text=a[i],fill='yellow',font=('', 20,'bold'))
    for i in range(5):
        b[i].config(command=math[i])
    
def b3():#进入大物实验
    a1(3,50,1000)
    d2=canvas.create_text(500,50,text='基于Python的专业辅助计算系统-->大物实验',fill='white',font=('', 20,'bold'))
    a=['杨氏模量拉伸法','元电荷测定-密立根油滴','光栅衍射','动态杨氏','实验查询']
    for i in range(5):
        d[i]=canvas.create_text(500,150+100*i,text=a[i],fill='yellow',font=('', 20,'bold'))
    for i in range(5):
        b[i].config(command=dwsy[i])
def b4():#进入数据处理
    a1(4,50,1000)
    data=[data1,data2,data3,data4,data5]
    d2=canvas.create_text(500,50,text='基于Python的专业辅助计算系统-->大数据处理',fill='white',font=('', 20,'bold'))
    a=['最小二乘拟合','数据降维','k均值聚类','...','...']
    for i in range(5):
        d[i]=canvas.create_text(500,150+100*i,text=a[i],fill='yellow',font=('', 20,'bold'))
    for i in range(5):
        b[i].config(command=data[i])
    
def b5():#进入图论
    a1(5,50,1000)
    tl=[tl1,tl2,tl3,tl4,tl5]
    d2=canvas.create_text(500,50,text='基于Python的专业辅助计算系统-->图论',fill='white',font=('', 20,'bold'))
    a=['二分图最大匹配','最小生成树','强连通图判断','最短路径','...']
    for i in range(5):
        d[i]=canvas.create_text(500,150+100*i,text=a[i],fill='yellow',font=('', 20,'bold'))
    for i in range(5):
        b[i].config(command=tl[i])


    
root = Tk()
canvas = Canvas(root,width = 1000, height = 666)
im2=PhotoImage(file='0053.gif')

im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image = im)
xt=canvas.create_text(500,50,text='基于Python的专业辅助计算系统',fill='white',font=('', 30,'bold'))
canvas.create_line(300,100,300,600,fill='white',width=10,dash=2)
canvas.create_line(780,100,780,600,fill='white',width=10,dash=2)
a=['科学计算器','高等数学&线性代数','大物实验','数据分析','图论']
b=[1,2,3,4,5]
d=[1,2,3,4,5]
c=[b1,b2,b3,b4,b5]

dwsy=[dwsy1,dwsy2,dwsy3,dwsy4,dwsy5]
math=[math1,math2,math3,math4,math5]
for i in range(6):
    canvas.create_line(200,100*i+100,800,100*i+100,fill='white',width=10)
    if i==5:break
    canvas.create_text(250,150+100*i,text=b[i],fill='white',width=10,font=('', 80))
    d[i]=canvas.create_text(500,150+100*i,text=a[i],fill='yellow',font=('', 25,'bold'))
    b[i]=Button(root,image=im2,command=c[i])
    b[i].place(x=50,y=100*i+100)
c2=Button(root,image=im3,command=a2)
c2.place(x=900,y=600)
canvas.pack()         
root.mainloop()



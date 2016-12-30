#coding=utf-8
import matplotlib.pyplot as plt  
import math  
import numpy
from Tkinter import *
import StringIO
from PIL import Image,ImageTk
import time
import os
def zjm2():
    c1=Button(fit,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    fit.destroy()
    os.system("menu.py")
def fitting():
#xa，ya待拟合数据
#order多项式阶数
    xa=(s1.get()).split(',')
    ya=(s2.get()).split(',')
    for i in range(len(xa)):
        xa[i]=eval(xa[i])
        ya[i]=eval(ya[i])
    
    order=eval(s3.get())
    fig = plt.figure(figsize=(7,3.5))
    ax = fig.add_subplot(111)
    ax.plot(xa,ya,'o')

#进行曲线拟合
    matA=[]  
    for i in range(0,order+1):  
        matA1=[]  
        for j in range(0,order+1):  
            tx=0.0  
            for k in range(0,len(xa)):  
                dx=1.0  
                for l in range(0,j+i):  
                    dx=dx*xa[k]  
                tx+=dx  
            matA1.append(tx)  
        matA.append(matA1)  
  
#print(len(xa))  
#print(matA[0][0])  
    matA=numpy.array(matA)  
  
    matB=[]  
    for i in range(0,order+1):  
        ty=0.0  
        for k in range(0,len(xa)):  
            dy=1.0
            for l in range(0,i):  
                dy=dy*xa[k]  
            ty+=ya[k]*dy  
        matB.append(ty)  
   
    matB=numpy.array(matB)  
    matAA=numpy.linalg.solve(matA,matB)  
  
#画出拟合后的曲线  
    #print(matAA)  #系数向量matAA
    xxa=xa  #设置拟合曲线x的输出范围 
    yya=[]  
    for i in range(0,len(xxa)):  
        yy=0.0  
        for j in range(0,order+1):  
            dy=1.0  
            for k in range(0,j):  
                dy*=xxa[i]  
            dy*=matAA[j]  
            yy+=dy  
        yya.append(yy)  
    ax.plot(xxa,yya,color='g')#linestyle='-',marker='')   
    ax.legend()
    plt.savefig('fit.jpg')
    image= Image.open("fit.jpg")
    pic=ImageTk.PhotoImage(image)   
    canvas.create_image(500,450,image=pic)
    
    s4=Entry(fit,width=70,font=('', 12 ,'bold'),bd=2)
    s4.place(x=300,y=235)
    s4.insert(END,matAA)
    
    canvas.pack()
    mainloop()


fit=Tk()
canvas = Canvas(fit,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')



c2=Button(fit,image=im3,command=zjm2).place(x=820,y=600)
canvas.create_image(500,333,image = im)
canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->最小二乘数据拟合',font=('', 20 ,'bold'),fill='white')
canvas.create_text(180,100,text='请输入数据，用逗号隔开',font=('', 20 ,'bold'),fill='white')
canvas.create_text(50,150,text='x:',font=('', 20 ,'bold'),fill='white')
canvas.create_text(50,200,text='y:',font=('', 20 ,'bold'),fill='white')
canvas.create_text(60,250,text='阶数:',font=('', 20 ,'bold'),fill='white')
canvas.create_text(250,250,text='结果:',font=('', 20 ,'bold'),fill='white')

Button(fit,text='拟合',font=('', 20 ,'bold'),bg='lightblue',width=5,command=fitting).place(x=860,y=155)
s1=Entry(fit,width=50,font=('', 20 ,'bold'),bd=2)
s1.place(x=80,y=135)
s1.insert(END,'1.01,2.58,4.1,5.45,6.99,8.28,9.2,9.45,9.58,9.66,9.72,9.86,9.93,10.02,10.06,10.08,10.09,10.11')

s2=Entry(fit,width=50,font=('', 20 ,'bold'),bd=2)
s2.place(x=80,y=185)
s2.insert(END,'153.52,389.58,611.72,808.78,1031.724,1207.224,1270.52,1155.735,1045.178,953.442,877.716,619.208,474.654,245.49,142.852,93.744,50.45,0')

s3=Entry(fit,width=5,font=('', 20 ,'bold'),bd=2)
s3.place(x=100,y=235)
s3.insert(END,'7')




canvas.pack()
mainloop()


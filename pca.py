#-*- coding:utf-8 -*-
from pylab import *
from numpy import *
from Tkinter import *
from PIL import Image,ImageTk   
import tkFileDialog
import csv
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
def pca(data,nRedDim=0,normalise=1):
   
    # 数据标准化
    m = mean(data,axis=0)
    data -= m
    # 协方差矩阵
    C = cov(transpose(data))
    # 计算特征值特征向量，按降序排序
    evals,evecs = linalg.eig(C)
    indices = argsort(evals)
    indices = indices[:-3:-1]
    evecs = evecs[:,indices]
    evals = evals[indices]
    if nRedDim>0:
        evecs = evecs[:,:nRedDim]
   
    if normalise:
        for i in range(shape(evecs)[1]):
            evecs[:,i] / linalg.norm(evecs[:,i]) * sqrt(evals[i])
    # 产生新的数据矩阵
    x = dot(transpose(evecs),transpose(data))
    # 重新计算原数据
    y=transpose(dot(evecs,x))+m    
    return x,y,evals,evecs
def pca1():
    global a,b,y
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    a=[]
    b=[]
    aa=[]
    csvfile=open('csv_test.csv','r')  #将100.csv中的数据放到一个二维列表中
    i=0
    for eachline in csvfile:
        x=eachline.split(',')
        if i==0:
            i=1
            continue
        aa.append(x)
        a.append(eval(x[0]))
        b.append(eval(x[1]))
    csvfile.close()
    figure(figsize=(7,4))

    data = zeros((len(a),2))
    data[:,0]=a

    data[:,1]=b
    x,y,evals,evecs = pca(data,1)




    plot(y[:,0],y[:,1],'+')
    plot(a,b,'.')
    xlabel('x')
    ylabel('y')
    savefig('pca.jpg')
    
    image= Image.open("pca.jpg")
    pic=ImageTk.PhotoImage(image)   
    canvas.create_image(500,310,image=pic)
    

    canvas.pack()
    mainloop()

    
def choosefile():
    filetext.delete(0,END)
    filename = tkFileDialog.askopenfilename()
    filetext.insert(END,filename)
    
def savefile():
    sfilename=tkFileDialog.asksaveasfilename()
    csvfile = file(sfilename, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['原始X','原始Y','新X','新Y'])
    for i in range(len(a)):
        data=[(a[i],b[i],y[i][0],y[i][1])]
        writer.writerows(data)
    csvfile.close()

root=Tk()
canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)

c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)

canvas.create_text(500,30,text='基于Python的专业辅助计算系统-->数据降维',font=('', 25 ,'bold'),fill='white')
canvas.create_text(500,70,text='主成分分析：PCA算法',font=('', 20 ,'bold'),fill='white')
canvas.create_text(225,545,text='文件路径：',font=('', 18 ,'bold'),fill='white')


i=170
j=300



filetext=Entry(root,font=('', 20 ,'bold'),width=28,bd=1)
filetext.place(x=110+i,y=230+j)
filetext.insert(END,'csv_test.csv')
Button(root,text='计算',command=pca1,font=('', 15 ,'bold'),bg='lightblue',width=10).place(x=50+i,y=300+j)
Button(root,text='选择文件',command=choosefile,font=('', 15 ,'bold'),bg='lightblue').place(x=550+i,y=230+j)
Button(root,text='保存',command=savefile,font=('', 15 ,'bold'),bg='lightblue',width=10).place(x=250+i,y=300+j)

exitbutton=Button(root,text='exit',command=root.destroy,font=('', 15 ,'bold'),bg='lightblue',width=10).place(x=50+400+i,y=300+j)

canvas.pack()
root.mainloop()




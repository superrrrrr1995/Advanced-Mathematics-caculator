
# -*- coding:utf-8 -*-
from Tkinter import *
import tkFileDialog
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
    
def floyd(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if (graph[j][i]+graph[i][k])<graph[j][k]:
                    graph[j][k]=graph[j][i]+graph[i][k]


def csh(n):
    global graph
    for i in range(1,n+1):
        graph[i]={}
        for j in range(1,n+1):
            graph[i][j]=0

def calc():
    global graph
    global searchfile

    n=int(searchfile.readline())
    csh(n)
    for i in range(n):
        line=searchfile.readline()
        l=line.split()
        vertex=int(l.pop(0))
        for x in l:
            adj_vertex,distance=map(int,x.split(","))
            graph[vertex][adj_vertex]=distance
    floyd(n)
    m=int(searchfile.readline())
    for i in range (m):
        line=searchfile.readline()
        l=line.split()
        a,b=int(l[0]),int(l[1])
        outputtext.insert(END,"%d号点与%d号点的最短距离为"%(a,b))
        outputtext.insert(END,graph[a][b])
        outputtext.insert(END,"\n")
        
def choosefile():
    global searchfile
    searchfile=tkFileDialog.askopenfile("r")
    str1=str(searchfile)
    flag=0
    lent=1
    str2={}
    lenn=len(str1)
    for i in range (lenn):
        t=str1[i]
        if flag==1:
            str2[lent]=(t)
            lent=lent+1
        if t=="'":
            flag=flag+1
    for i in range(1,lent-1):
        filetext.insert(END,str(str2[i]))
    
def returns():
    root.destroy()
    os.system("main.py")


global searchfile
graph={}
root=Tk()
canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)
#root.geometry('400x300')
im3=PhotoImage(file='3.gif')
c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)

canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->zdllj',font=('', 20 ,'bold'),fill='green')
canvas.create_text(500,70,text='求某张图上某地到某地的最短路径问题',font=('', 20 ,'bold'),fill='green')
canvas.create_text(250,110,text='算法简介：',font=('', 18 ,'bold'),fill='yellow')
canvas.create_text(250,330,text='计算结果：',font=('', 18 ,'bold'),fill='yellow')




i=170
j=230


canvas.create_text(225,445+30+230-j,text='文件路径：',font=('', 18 ,'bold'),fill='yellow')

introduce=Text(root,height=10,bd=5)
introduce.place(x=170,y=130)
introduce.insert(END,'floyd：通过一个图的权值矩阵求出它的每两点间的最短路径行成的矩阵。从图的带权邻接矩阵A=[a(i,j)] n×n开始，递归地进行n次更新，即由矩阵D(0)=A，按一个公式，构造出矩阵D(1)；又用同样地公式由D(1)构造出D(2)；……；最后又用同样的公式由D(n-1)构造出矩阵D(n)。矩阵D(n)的i行j列元素便是i号顶点到j号顶点的最短路径长度，称D(n)为图的距离矩阵，同时还可引入一个后继节点矩阵path来记录两点间的最短路径。采用的是(松弛技术)，对在i和j之间的所有其他点进行一次松弛。所以时间复杂度为O(n^3)')
outputtext=Text(root,height=5,bd=5)
outputtext.place(x=170,y=350)


filetext=Text(root,font=('', 20 ,'bold'),height=1,width=28,bd=1)
filetext.place(x=110+i,y=230+j)

Button(root,text='计算',command=calc,font=('', 15 ,'bold'),bg='orange',width=10).place(x=50+i,y=300+j)
Button(root,text='选择文件',command=choosefile,font=('', 15 ,'bold'),bg='orange').place(x=550+i,y=230+j)

exitbutton=Button(root,text='退出',command=root.destroy,font=('', 15 ,'bold'),bg='orange',width=10).place(x=50+400+i,y=300+j)
returnbutton=Button(root,text='返回',command=returns,font=('', 15 ,'bold'),bg='orange',width=10).place(x=50+200+i,y=300+j)
canvas.pack()
root.mainloop()
    








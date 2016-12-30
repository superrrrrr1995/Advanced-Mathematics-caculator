
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
    
def dfs(u):
    global graph,searchfile,n1,n2,m,linker,used
    for v in range(1,n1+1):
        if graph[u][v] and used[v]==0:
            used[v]=1
            if(linker[v]==-1 or dfs(linker[v])):
                linker[v]=u

                return 1
    return 0
    
def hungary():
    global graph,searchfile,n1,n2,m,linker,used
    res=0
    u=0
    cshlinker()
    for u in range(1,n1+1):
        cshused()
        if(dfs(u)!=0):
            res=res+1
    return res
    
def csh():
    global graph,searchfile,n1,n2,m
    for i in range(2020):
        graph[i]={}
        for j in range(2020):
            graph[i][j]=0

def calc():
    global graph,searchfile,n1,n2,m
    m=int(searchfile.readline())
    csh()
    n1=int(searchfile.readline())
    n2=int(searchfile.readline())
    for i  in range(m):
        line=searchfile.readline()
        l=line.split()
        u,v=int(l[0]),int(l[1])
        graph[u][v]=1
    outputtext.insert(END,"%d\n"%hungary())


    
def cshlinker():
    global graph,searchfile,n1,n2,m,linker
    for i in range(2020):
        linker[i]=-1

def cshused():
    global graph,searchfile,n1,n2,m,linker,used
    for i  in range(2020):
        used[i]=0
        
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


global graph,searchfile,n1,n2,m,linker,used 
used={}
linker={}
graph={}
root=Tk()
canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)

im3=PhotoImage(file='3.gif')
c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)

canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->hungary',font=('', 20 ,'bold'),fill='green')
canvas.create_text(500,70,text='求二分图最大匹配问题',font=('', 20 ,'bold'),fill='green')
canvas.create_text(250,110,text='算法简介：',font=('', 18 ,'bold'),fill='yellow')
canvas.create_text(250,330,text='计算结果：',font=('', 18 ,'bold'),fill='yellow')




i=170
j=230


canvas.create_text(225,445+30+230-j,text='文件路径：',font=('', 18 ,'bold'),fill='yellow')

introduce=Text(root,height=10,bd=5)
introduce.place(x=170,y=130)
introduce.insert(END,'匈牙利算法：如果图G=(V,E)的顶点集何V可分为两个集合X,Y，且满足 X∪Y = V, X∩Y=Φ，则G称为二部图；图G的边集用E(G)表示。而最大匹配求的是最大的边集M，是E（G）的子集是的M中任意两条边在图上均不邻接')
outputtext=Text(root,height=5,bd=5)
outputtext.place(x=170,y=350)


filetext=Text(root,font=('', 20 ,'bold'),height=1,width=28,bd=1)
filetext.place(x=110+i,y=230+j)

Button(root,text='计算',command=calc,font=('', 15 ,'bold'),bg='orange',width=10).place(x=50+i,y=300+j)
Button(root,text='选择文件',command=choosefile,font=('', 15 ,'bold'),bg='orange').place(x=550+i,y=230+j)

exitbutton=Button(root,text='exit',command=root.destroy,font=('', 15 ,'bold'),bg='orange',width=10).place(x=50+400+i,y=300+j)
returnbutton=Button(root,text='return',command=returns,font=('', 15 ,'bold'),bg='orange',width=10).place(x=50+200+i,y=300+j)
canvas.pack()
root.mainloop()
    



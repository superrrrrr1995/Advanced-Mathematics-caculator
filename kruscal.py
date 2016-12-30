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
    
def csh():
    global graph
    global n,m
    for i in range(1,n+1):
        graph[i]={}
        for j in range(1,n+1):
            graph[i][j]=0
def cshn():
    global visit
    global u
    global v
    global n,m
    global dis
    for i in range(n+1):
        visit[i]=0
        u[i]=0
        v[i]=0
        dis[i]=0
def findfather(x):
    global p
    if (p[x]==x) :
        return x
    else:
        return findfather(p[x])
def kruscal():
    global graph
    global visit
    global n,m
    cou=0
    ans=0
    global p
    p={}
    r={}
    for i in range(2*n):
        p[i]=i
    for  i in range(2*m):  
        r[i]=i
    for i in range(0,m-1):
        for j in range(i+1,m):
            if dis[r[i]]>dis[r[j]]:
                print dis[r[i]],dis[r[j]]
                t=r[i]
                r[i]=r[j]
                r[j]=t
    for i in range(0,m):
        print r[i],
    for i in range(0,m):
        e=r[i]
        x=findfather(u[e])
        y=findfather(v[e])
        if x!=y:
            ans=ans+dis[e]
            p[x]=y
            cou=cou+1
    if cou<n-1:
        ans=0
    return ans
        
    
    
def calc():
    global searchfile
    global u,v,dis
    global n,m
    u={}
    v={}
    dis={}
    n=int(searchfile.readline())




    csh()
    m=int(searchfile.readline())
    cshn()
    for i in range (m):
        line=searchfile.readline()
        l=line.split()
        print l[0],l[1],l[2]
        u[i]=int(l[0])
        v[i]=int(l[1])
        dis[i]=int(l[2])
    outputtext.insert(END,"%d\n"%kruscal())
    
        
def choosefile():
    filetext.delete(1.0,END)
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
visit={}
    
root=Tk()
canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)

im3=PhotoImage(file='3.gif')
c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)

canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->kruscal',font=('', 20 ,'bold'),fill='green')
canvas.create_text(500,70,text='某张图上使得所有点联通的最少的路径（最小生成树）',font=('', 15 ,'bold'),fill='green')
canvas.create_text(250,110,text='算法简介：',font=('', 18 ,'bold'),fill='yellow')
canvas.create_text(250,330,text='计算结果：',font=('', 18 ,'bold'),fill='yellow')




i=170
j=230


canvas.create_text(225,445+30+230-j,text='文件路径：',font=('', 18 ,'bold'),fill='yellow')

introduce=Text(root,height=10,bd=5)
introduce.place(x=170,y=130)
introduce.insert(END,'kruscal:每次选择图上未选择的最短的边加入已选择边的集合中，若加入后已选择边集合产生回路则舍弃这条边，最终一共选择n-1条边这个集合就为原图的最小生成树')
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
    




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
    
def tarjan(u):
    global n,m,Bcnt,Top,Index,belong,stack,instack,graph,low,dfn
    stack[Top]=u
    Top=Top+1
    instack[u]=1
    Index=Index+1
    low[u]=Index
    dfn[u]=Index
    for i in range(n+1):
        if(graph[u][i]==1):
            if(dfn[i]==0):
                tarjan(i)
                if(low[u]>low[i]):
                    low[u]=low[i]
            else :
                if(instack[i]==1):
                    if(low[u]>dfn[i]):
                        low[u]=low[i]
    if(low[u]==dfn[u]):
        
        Bcnt=Bcnt+1
        v=-1
        while u!=v:
            Top=Top-1
            v=stack[Top]
            instack[v]=0
            belong[v]=Bcnt
    

def csh():
    global n,m,Bcnt,Top,Index,belong,stack,instack,graph,low,dfn
    low={}
    dfn={}
    belong={}
    instack={}
    stack={}
    for i in range(0,n+1):
        graph[i]={}
        for j in range(0,n+1):
            graph[i][j]=0
    Bcnt=0
    Top=0
    Index=0
    for i in range(n+1):
        low[i]=0
        dfn[i]=0

def calc():
    global n,m,Bcnt,Top,Index,belong,stack,instack,graph,low,dfn
    n=int(searchfile.readline())
    csh()
    m=int(searchfile.readline())
    for i in range(m):
        line=searchfile.readline()
        l=line.split()
        a,b=int(l[0]),int(l[1])
        graph[a][b]=1
    for i in range(1,n+1):
        if(dfn[i]==0
           ):
            tarjan(1)
    if(Bcnt==1):
        outputtext.insert(END,'YES')
    else :
        outputtext.insert(END,'NO')
    
        
    
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
    



global searchfile
graph={}
    
root=Tk()
canvas = Canvas(root,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image=im)

im3=PhotoImage(file='3.gif')
c2=Button(root,image=im3,command=zjm2).place(x=820,y=600)

canvas.create_text(500,30,text='基于Python的专业辅助计算系统-->tarjan',font=('', 25 ,'bold'),fill='white')
canvas.create_text(500,70,text='求某张图是不是强连通图',font=('', 20 ,'bold'),fill='white')
canvas.create_text(250,110,text='算法简介：',font=('', 18 ,'bold'),fill='white')
canvas.create_text(250,330,text='计算结果：',font=('', 18 ,'bold'),fill='white')




i=170
j=230


canvas.create_text(225,445+30+230-j,text='文件路径：',font=('', 18 ,'bold'),fill='white')

introduce=Text(root,height=10,bd=5)
introduce.place(x=170,y=130)
introduce.insert(END,'Tarjan强连通分量算法：Tarjan算法基于定理：在任何深度优先搜索中，同一强连通分量内的所有顶=点均在同一棵深度优先搜索树中。也就是说，强连通分量一定是有向图的某个深搜树子树。可以证明，当一个点既是强连通子图Ⅰ中的点，又是强连通子图Ⅱ中的点，则它是强连通子图Ⅰ∪Ⅱ中的点。这样，我们用low值记录该点所在强连通子图对应的搜索子树的根节点的Dfn值。注意，该子树中的元素在栈中一定是相邻的，且根节点在栈中一定位于所有子树元素的最下方。强连通分量是由若干个环组成的。所以，当有环形成时（也就是搜索的下一个点已在栈中），我们将这一条路径的low值统一，即这条路径上的点属于同一个强连通分量。如果遍历完整个搜索树后某个点的dfn值等于low值，则它是该搜索子树的根。这时，它以上（包括它自己）一直到栈顶的所有元素组成一个强连通分量。')

outputtext=Text(root,height=5,bd=5)
outputtext.place(x=170,y=350)


filetext=Text(root,font=('', 20 ,'bold'),height=1,width=28,bd=1)
filetext.place(x=110+i,y=230+j)

Button(root,text='计算',command=calc,font=('', 15 ,'bold'),bg='lightblue',width=10).place(x=50+50+i,y=300+j)
Button(root,text='选择文件',command=choosefile,font=('', 15 ,'bold'),bg='lightblue').place(x=550+i,y=230+j)

exitbutton=Button(root,text='退出',command=root.destroy,font=('', 15 ,'bold'),bg='lightblue',width=10).place(x=400+i,y=300+j)
canvas.pack()
root.mainloop()
    



#coding=utf*8
from Tkinter import *
import numpy as np
import time
import os
import sqlite3 #导入模块  #

def sql_matrix(x):
    try:
    
        a0=str(x)
        a1=str(x.T)
        a2=str(x.trace())
        a3=str(np.linalg.det(x))
        a4=str(np.linalg.norm(x,ord=None))
        a5=str(np.linalg.eig(x))
        a6=str(np.linalg.inv(x))
        a7=str(np.linalg.cond(x,p=None))
    except:
        pass
    
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table matrix ( 矩阵 varchar(10) primary key, 转置 varchar(10), 迹 varchar(10),行列式 varchar(10),范数 varchar(10) ,特征值、特征向量 varchar(10) ,逆矩阵 varchar(10) ,条件数 varchar(10)  )""")
    except:
        pass
    try:
        for t in[(a0,a1,a2,a3,a4,a5,a6,a7)]:    
            cx.execute("insert into matrix values (?,?,?,?,?,?,?,?)", t)
    except:
        pass
    cx.commit()



sql_matrix('1 0 0\n0 1 0\n0 0 1\n')
def zjm2():
    c1=Button(math4,image=im3)
    c1.update()
    for a in range(820,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    math4.destroy()
    os.system("menu.py")
def b231():
    pass
def b220():
    global x
    a=jz.get(1.0,END)
    a=a.split('\n')
    j=[]
    for i in range(len(a)-1):
        j.append(a[i].split(' '))
    x=np.array(j,dtype=np.float)
    sql_matrix(x)
def b221():
    b220()
    global i0
    ans.append(1)
    ans[i0]=x.T
    outputbox.insert(END,'ans[%d]=转置xT=:\n'%(i0))
    outputbox.insert(END,x.T) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b222():
    b220()
    global i0
    ans.append(1)
    ans[i0]=x.trace()
    outputbox.insert(END,'ans[%d]=迹tr[X]=:\n'%(i0))
    outputbox.insert(END,x.trace()) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b223():
    b220()
    global i0
    ans.append(1)
    ans[i0]=np.linalg.det(x)
    outputbox.insert(END,'ans[%d]=行列式det[X]：\n'%(i0))
    outputbox.insert(END,np.linalg.det(x)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b224():
    b220()
    global i0
    ans.append(1)
    ans[i0]=np.linalg.norm(x,ord=None)
    outputbox.insert(END,'ans[%d]=范数：\n'%(i0))
    outputbox.insert(END,np.linalg.norm(x,ord=None)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b225():
    b220()
    global i0
    ans.append(1)
    ans[i0]=np.linalg.eig(x)
    outputbox.insert(END,'ans[%d]=特征值&特征向量:\n'%(i0))
    outputbox.insert(END,np.linalg.eig(x)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b226():
    b220()
    global i0
    ans.append(1)
    ans[i0]=np.linalg.inv(x)
    outputbox.insert(END,'ans[%d]=逆矩阵X^-1:\n'%(i0))
    outputbox.insert(END,np.linalg.inv(x)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b227():
    b220()

    global i0
    ans.append(1)
    ans[i0]=np.linalg.cond(x,p=None)
    outputbox.insert(END,'ans[%d]=条件数:\n'%(i0))
    outputbox.insert(END,np.linalg.cond(x,p=None)) 
    outputbox.insert(END,'\n')
    i0=i0+1
    
def b230():
    global A,B
    a=jz1.get(1.0,END)
    b=jz2.get(1.0,END)
    a=a.split('\n')
    b=b.split('\n')
    j1=[];j2=[]
    for i in range(len(a)-1):
        j1.append(a[i].split(' '))
        j2.append(b[i].split(' '))
    A=np.array(j1,dtype=np.float)
    B=np.array(j2,dtype=np.float)
def b231():
    b230()
    global i0
    ans.append(1)
    ans[i0]=eval(js.get())
    a='ans[%d]=%s\n'%(i0,js.get())
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1
i0=0
ans=[]
global jz1,jz2,js
math4 = Tk()
b=400
canvas = Canvas(math4,width = 1000, height = 666)
im3=PhotoImage(file='3.gif')
c2=Button(math4,image=im3,command=zjm2).place(x=820,y=600)
im=PhotoImage(file='bg.gif')
a=100

#canvas.create_image(500,333,image = im)
#xt=canvas.create_text(500,50,text='微积分运算',fill='white',font=('', 50))
Label(math4,text='线性代数',font=('',25,'bold'),fg='brown').place(x=400,y=20)
Label(math4,text='矩阵A',font=('',15,'bold'),fg='blue').place(x=50+b,y=20+a)
Label(math4,text='矩阵B',font=('',15,'bold'),fg='blue').place(x=50+b,y=160+a)
Label(math4,text='矩阵C',font=('',15,'bold'),fg='blue').place(x=50+b,y=300+a+70)

jz1=Text(math4,width=20,height=6)
jz1.place(x=10+b,y=50+a)
jz1.insert(END,'1 0 0\n0 1 0\n0 0 1')

jz2=Text(math4,width=20,height=6)
jz2.place(x=10+b,y=190+a)
jz2.insert(END,'1 2 3\n0 1 2\n3 0 1')

jz=Text(math4,width=20,height=6)
jz.place(x=10+b,y=330+a+70)
jz.insert(END,'1 0 0\n0 1 0\n0 0 1')

Label(math4,text='矩阵运算',font=('',20,'bold'),fg='brown').place(x=250+b,y=0+a)

Label(math4,text='运算符号：',font=('',15,'bold'),fg='blue').place(x=200+b,y=50+a)
Label(math4,text='运算表达式：',font=('',15,'bold'),fg='blue').place(x=200+b,y=200+a)
    
t=['内积:dot(A,B)','外积:outer(A,B)','乘方X**Y','加法：+','减法：-','乘法：*']

for i in range(3):
    Label(math4,text=t[i],font=('',15,'bold'),fg='orange').place(x=250+b,y=100+30*i+a)
    Label(math4,text=t[i+3],font=('',15,'bold'),fg='orange').place(x=250+180+b,y=100+30*i+a)

js=Entry(math4,width=20,font=('', 20))
js.place(x=220+b,y=250+a)
js.insert(END,'A*B')

Label(math4,text='矩阵C特性',font=('',20,'bold'),fg='brown').place(x=250+b,y=330+a)
c=[b221,b222,b223,b224,b225,b226,b227]
t=['转置XT','迹tr[X]','行列式det(X)','范数','特征值,特征向量','逆矩阵X^-1','条件数']
for i in range(4):
    Checkbutton(math4,text=t[i],font=('',15,'bold'),fg='blue',command=c[i]).place(x=400+200,y=480+30*i)
for i in range(4,7):
    Checkbutton(math4,text=t[i],font=('',15,'bold'),fg='blue',command=c[i]).place(x=400+200+150,y=360+30*i)

Label(math4,text='输出框',font=('',20,'bold'),fg='brown').place(x=150,y=100)
outputbox=Text(math4,width=40,height=25,bd=5)
outputbox.place(x=20,y=160) #输出

Button(math4,text='计算',font=('',15,'bold'),fg='red',command=b231).place(x=520+b,y=250+a)
canvas.pack()
mainloop()



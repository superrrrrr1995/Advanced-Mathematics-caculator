# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time

from tkMessageBox import*
import numpy as np
from sympy import *
import sqlite3

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
def sql(f,d1,d2,n):
    try:
        x=Symbol('x')
        f=eval(f)
        a1=str(f)
        a2=str(diff(f,x))
        a3=str(integrate(f,x))
        a4=str(integrate(f,(x,d1,d2)))
        a5=str(solve(f,x))
        a6=str(f.series(x,0,n))

    except:
        pass
    
    cx = sqlite3.connect("./sqlite/data.db")
    cu=cx.cursor()
    try:
        cu.execute("""create table function ( function primary key, 解析式 varchar(10), 定义域 varchar(10),导函数 varchar(10),不定积分 varchar(10) ,定积分 varchar(10) ,零点 varchar(10) ,泰勒展开 varchar(10)  )""")
    except:
        pass
    try:
        for t in[('%s,%s,%s'%(a1,d1,d2),a1,'[%s,%s]'%(d1,d2),a2,a3,a4,a5,a6)]:    
            cx.execute("insert into function values (?,?,?,?,?,?,?,?)", t)
    except:
        print 'error'
    cx.commit()

def a2():#后退小车左移动
    c1=Button(kxjsq,image=im3)
    c1.update()
    for a in range(900,0,-1):        
        c1.place(x=a,y=600)
        c1.update()
        time.sleep(0.0001)
    kxjsq.destroy()
    os.system("menu.py")

def b110():
    x = Symbol('x')
    global i0
    ans.append(1)
    ans[i0]=integrate(eval(e4.get()),x)
    x='ans[%d]=积分(%s)='%(i0,e4.get())
    outputbox.insert(END,x)
    outputbox.insert(END,ans[i0])
    outputbox.insert(END,'\n')
    i0=i0+1
    sql(e4.get(),0,1,5)
def b11():
    global e4
    root = Toplevel()
    Canvas(root,width=600,height=300).pack()
    Label(root,text='不定积分',font=('',20,'bold'),fg='green').place(x=50,y=20)
    Label(root,text='∫',font=('',100)).place(x=0,y=50)
    e4=Entry(root,width=8,font=('',50))
    e4.place(x=150,y=100)
    e4.insert(END,'x')
    Label(root,text='dx',font=('',100)).place(x=400,y=50)
    Button(root,text='计算',font=('',20,'bold'),fg='red',command=b110).place(x=450,y=250)
    mainloop()
    

def b121():
    x = Symbol('x')
    global i0
    ans.append(1)
    ans[i0]=integrate(eval(e3.get()), (x,eval(e2.get()) ,eval(e1.get())))
    x='ans[%d]=积分(%s),x∈[%s,%s]\n    ='%(i0,e3.get(),e2.get(),e1.get())
    outputbox.insert(END,x)
    outputbox.insert(END,ans[i0])
    outputbox.insert(END,'\n')
    i0=i0+1
    sql(e3.get(),eval(e2.get()) ,eval(e1.get()),5)       
def b12():
    global e1,e2,e3
    root = Toplevel()
    Canvas(root,width=600,height=300).pack()
    Label(root,text='数值积分',font=('',20,'bold'),fg='green').place(x=50,y=20)
    Label(root,text='∫',font=('',100)).place(x=0,y=50)
    e1=Entry(root,width=2,font=('',20))
    e1.insert(END,10)
    e1.place(x=110,y=70)
    e2=Entry(root,width=2,font=('',20))
    e2.place(x=100,y=140)
    e2.insert(END,1)
    e3=Entry(root,width=8,font=('',50))
    e3.place(x=150,y=100)
    e3.insert(END,'x')
    Label(root,text='dx',font=('',100)).place(x=400,y=50)
    Button(root,text='计算',font=('',20,'bold'),fg='red',command=b121).place(x=450,y=250)
    mainloop()

def b130():
    x = Symbol('x')
    global i0
    ans.append(1)
    ans[i0]=diff(eval(e3.get()),x)
    x='ans[%d]=导数(%s)='%(i0,e3.get())
    outputbox.insert(END,x)
    outputbox.insert(END,ans[i0])
    outputbox.insert(END,'\n')
    i0=i0+1
    sql(e3.get(),0,1,5)
    
def b13():
    global e3
    root = Toplevel()
    c=Canvas(root,width=600,height=300)    
    Label(root,text='导函数',font=('',20,'bold'),fg='green').place(x=50,y=20)    
    c.create_text(70,80,text='d',fill='black',font=('',50))
    c.create_text(70,180,text='dx',fill='black',font=('',50))    
    e3=Entry(root,width=8,font=('',50))
    e3.place(x=150,y=100)
    e3.insert(END,'x')
    c.create_text(70,100,text='___',fill='black',font=('',50))
    Button(root,text='计算',font=('',20,'bold'),fg='red',command=b130).place(x=450,y=250)
    c.pack()
    mainloop()

def b14():
    global t41,t42,t43,t44
    root=Tk()
    Label(root,text=u'数列求和'.encode("UTF-8"),font=(', 20')).grid(row=0,column=0,columnspan=2)
    t43=Text(root,width=3,height=1,font=(', 20'))
    t43.insert(END,100)
    
    t43.grid(row=1,column=0,columnspan=3)
    Label(root,text=u'∑'.encode("UTF-8"),font=(', 100')).grid(row=2,column=0,columnspan=3)
    t41=Entry(root,bd=10,font=(', 50'),width=8)
    t41.grid(row=2,column=3,columnspan=3)
    t41.insert(END,'n')

    Label(root,text='n=',font=(', 20')).grid(row=3,column=0)
    t42=Text(root,width=2,height=1,font=(', 20'))
    t42.grid(row=3,column=1)
    t42.insert(END,1)
    Label(root,text='step=',font=(', 20')).grid(row=3,column=3)
    t44=Text(root,width=2,height=1,font=(', 20'))
    t44.grid(row=3,column=4)
    t44.insert(END,1)

    Button(root,text='计算',font=(', 20'),fg='blue',command=b141).grid(row=4,column=6)
    mainloop()
def b141():
    a=eval(t42.get(1.0,END))
    b=eval(t43.get(1.0,END))
    c=eval(t44.get(1.0,END))
    d=t41.get()
    s=0
    s0=[]
    for n in range(a,b+1,c):
        s=s+eval(d)
        s0.append(eval(d))
    global i0
    ans.append(1)
    ans[i0]=s
    x='ans[%d]=%f+%f+...+%f\n    ='%(i0,s0[0],s0[1],s0[b-1])

    outputbox.insert(END,x)
    outputbox.insert(END,s)
    outputbox.insert(END,'\n')
    i0=i0+1
        
def b15():
    global t51,t52,t53,t54
    root=Tk()
    Label(root,text=u'累乘'.encode("UTF-8"),font=(', 20')).grid(row=0,column=0,columnspan=2)
    t53=Text(root,width=3,height=1,font=(', 20'))
    t53.grid(row=1,column=0,columnspan=3)
    t53.insert(END,10)
    Label(root,text=u'∏'.encode("UTF-8"),font=(', 100')).grid(row=2,column=0,columnspan=3)
    t51=Entry(root,bd=10,font=(', 50'),width=8)
    t51.grid(row=2,column=3,columnspan=3)
    t51.insert(END,'n')
    Label(root,text='n=',font=(', 20')).grid(row=3,column=0)
    t52=Text(root,width=2,height=1,font=(', 20'))
    t52.grid(row=3,column=1)
    t52.insert(END,1)
    Label(root,text='step=',font=(', 20')).grid(row=3,column=3)
    t54=Text(root,width=2,height=1,font=(', 20'))
    t54.grid(row=3,column=4)
    t54.insert(END,1)

    Button(root,text='计算',font=(', 20'),fg='blue',command=b151).grid(row=4,column=6)
    mainloop()
def b151():
    a=eval(t52.get(1.0,END))
    b=eval(t53.get(1.0,END))
    c=eval(t54.get(1.0,END))
    d=t51.get()
    s=1
    s0=[]
    for n in range(a,b+1,c):
        s=s*eval(d)
        s0.append(eval(d))

    global i0
    ans.append(1)
    ans[i0]=s
    x='ans[%d]=%f*%f*...*%f\n    ='%(i0,s0[0],s0[1],s0[b-1])
    outputbox.insert(END,x)
    outputbox.insert(END,s)
    outputbox.insert(END,'\n')
    i0=i0+1
def b210():
    global a,s
    a=tj.get(1.0,END)
    a=a.split('\n')
    a.pop()
    a=np.array(a,dtype=np.float)
    s=0
    for j in range(len(a)):
        s=(a[j]-float(sum(a))/len(a))**2+s
def b211():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=最大值&最小值:\n'%(i0))
    outputbox.insert(END,'%f,%f'%(max(a),min(a))) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b212():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=求和:\n'%(i0))
    outputbox.insert(END,sum(a)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b213():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=平均数：\n'%(i0))
    outputbox.insert(END,float(sum(a))/len(a)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b214():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=总体方差：\n'%(i0))
    outputbox.insert(END,float(s)/len(a)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b215():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=总体标准差:\n'%(i0))
    outputbox.insert(END,sqrt(float(s)/len(a))) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b216():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=样本方差:\n'%(i0))
    outputbox.insert(END,float(s)/(len(a)-1)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b217():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=样本标准差:\n'%(i0))
    outputbox.insert(END,sqrt(float(s)/(len(a)-1))) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b218():
    b210()
    global i0
    ans.append(1)
    outputbox.insert(END,'ans[%d]=极差:\n'%(i0))
    outputbox.insert(END,max(a)-min(a)) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b21():
    global tj
    root=Tk()
    Canvas(root,width=600,height=300).pack()
    tj=Text(root,width=40,height=15)
    tj.place(x=10,y=50)
    tj.insert(END,'1\n2\n3\n4\n5')
    Label(root,text='统计',font=('',20,'bold'),fg='green').place(x=250,y=0)
    c=[b211,b212,b213,b214,b215,b216,b217,b218]
    t=['最大值&最小值','求和','平均数','总体方差','总体标准差','样本方差','样本标准差','极差']
    for i in range(8):
        Checkbutton(root,text=t[i],font=('',13,'bold'),fg='blue',command=c[i]).place(x=370,y=50+25*i)
    mainloop()
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
def b22():
    global jz
    root=Tk()
    Canvas(root,width=600,height=300).pack()
    jz=Text(root,width=40,height=15)
    jz.place(x=10,y=50)
    jz.insert(END,'1 0 0\n0 1 0\n0 0 1')
    Label(root,text='矩阵特性',font=('',20,'bold'),fg='green').place(x=250,y=0)
    c=[b221,b222,b223,b224,b225,b226,b227]
    t=['转置XT','迹tr[X]','行列式det(X)','范数','特征值,特征向量','逆矩阵X^-1','条件数']
    for i in range(7):
        Checkbutton(root,text=t[i],font=('',15,'bold'),fg='blue',command=c[i]).place(x=350,y=50+30*i)
    mainloop()
    
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
    sql_matrix(A)
    sql_matrix(B)
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
def b23():
    global jz1,jz2,js
    root=Tk()
    Canvas(root,width=600,height=300).pack()
    Label(root,text='矩阵A',font=('',15,'bold'),fg='blue').place(x=50,y=20)
    Label(root,text='矩阵B',font=('',15,'bold'),fg='blue').place(x=50,y=150)

    jz1=Text(root,width=20,height=6)
    jz1.place(x=10,y=50)
    jz1.insert(END,'1 0 0\n0 1 0\n0 0 1')

    jz2=Text(root,width=20,height=6)
    jz2.place(x=10,y=180)
    jz2.insert(END,'1 2 3\n0 1 2\n3 0 1')

    Label(root,text='矩阵运算',font=('',20,'bold'),fg='green').place(x=250,y=0)

    Label(root,text='运算符号：',font=('',15,'bold'),fg='blue').place(x=200,y=50)
    Label(root,text='运算表达式：',font=('',15,'bold'),fg='blue').place(x=200,y=200)
    
    t=['内积:dot(A,B)','外积:outer(A,B)','乘方X**Y','加法：+','减法：-','乘法：*']

    for i in range(3):
        Label(root,text=t[i],font=('',15,'bold'),fg='orange').place(x=250,y=100+30*i)
        Label(root,text=t[i+3],font=('',15,'bold'),fg='orange').place(x=250+180,y=100+30*i)

    js=Entry(root,width=20,font=('', 20))
    js.place(x=220,y=250)
    js.insert(END,'A*B')
    Button(root,text='计算',font=('',15,'bold'),fg='red',command=b231).place(x=520,y=250)
    mainloop()



def b241():
    x = Symbol("x")
    global i0
    ans.append(1)
    ans[i0]=solve(eval(fc.get()), x)
    a='ans[%d]=fsolve(%s=0)\n    ='%(i0,fc.get())
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1   
def b24():
    global fc
    root = Tk()
    Canvas(root,width=600,height=300).pack()
    Label(root,text='一元方程',font=('',20,'bold'),fg='green').place(x=250,y=20)
    Label(root,text='方程:',font=('',20,'bold'),fg='blue').place(x=20,y=120)
    Label(root,text='=0',font=('',20,'bold'),fg='blue').place(x=520,y=120)

    fc=Entry(root,width=12,font=('',50))
    fc.place(x=100,y=100)
    fc.insert(END,'x**2-1')
    Button(root,text='计算',font=('',20,'bold'),fg='red',command=b241).place(x=450,y=250)
    mainloop()



def b251():
    global fcz
    global i0
    x1 = Symbol("x1")
    x2 = Symbol("x2")
    x3 = Symbol("x3")
    x4 = Symbol("x4")
    x5 = Symbol("x5")
    ans.append(1)
    ans[i0]=solve([eval(fcz[0].get()),eval(fcz[1].get()),eval(fcz[2].get()),eval(fcz[3].get()),eval(fcz[4].get())], [x1,x2,x3,x4,x5])
    a='ans[%d]=fsolve(%s,%s,%s,%s,%s=0)\n    ='%(i0,fcz[0].get(),fcz[1].get(),fcz[2].get(),fcz[3].get(),fcz[4].get())
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1   
    
def b25():
    global fcz
    root = Tk()
    Canvas(root,width=600,height=300).pack()
    Label(root,text='方程组',font=('',20,'bold'),fg='green').place(x=250,y=20)
    fcz=[0 for i in range(5)]
    fcz0=['x1','x2','x3','x4','x5']
    for i in range(5):
        fcz[i]=Entry(root,width=15,font=('',20))
        fcz[i].place(x=100,y=60+50*i)
        fcz[i].insert(END,fcz0[i])
        Label(root,text='=0',font=('',20,'bold'),fg='blue').place(x=320,y=60+50*i)
        Label(root,text='%d:'%(i+1),font=('',20,'bold'),fg='blue').place(x=30,y=60+50*i)
    Button(root,text='计算',font=('',20,'bold'),fg='red',command=b251).place(x=450,y=250)
    mainloop()


def b31():
    inputbox.insert(INSERT,'sin()')
def b32():
    inputbox.insert(INSERT,'cos()')
def b33():
    inputbox.insert(INSERT,'tan()')
def b34():
    inputbox.insert(INSERT,'log(,)')
def b35():
    inputbox.insert(INSERT,'abs()')
    
def b41():
    inputbox.insert(INSERT,'asin()')
def b42():
    inputbox.insert(INSERT,'acos()')
def b43():
    inputbox.insert(INSERT,'atan()')
def b44():
    inputbox.insert(INSERT,'sqrt()')
def b45():
    inputbox.insert(INSERT,'**')

def b51():
    inputbox.insert(INSERT,'P(,)')
def b52():
    inputbox.insert(INSERT,'C(,)')
def b53():
    global i0
    ans.append(1)
    ans[i0]=Rational(ans[i0-1])
    a='ans[%d]=ans[%d]='%(i0,i0-1)
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1   

def b54():
    global i0
    ans.append(1)
    ans[i0]=(ans[i0-1]).evalf()
    a='ans[%d]=ans[%d]='%(i0,i0-1)
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1 

def b55():
    inputbox.insert(INSERT,' ')#待定
    
def b61():
    inputbox.insert(INSERT,'pi')
def b62():
    inputbox.insert(INSERT,'E')
def b63():
    inputbox.insert(INSERT,'(')
def b64():
    inputbox.insert(INSERT,')')
def b65():
    inputbox.insert(INSERT,'factorial()')
    
def b71():
    inputbox.insert(INSERT,'1')
def b72():
    inputbox.insert(INSERT,'2')
def b73():
    inputbox.insert(INSERT,'3')
def b74(): #删除末端元素
    a=len(inputbox.get())
    inputbox.delete(a-1,a)
def b75():
    inputbox.delete(0,END)
    
def b81():
    inputbox.insert(INSERT,'4')
def b82():
    inputbox.insert(INSERT,'5')
def b83():
    inputbox.insert(INSERT,'6')
def b84():
    inputbox.insert(INSERT,'*')
def b85():
    inputbox.insert(INSERT,'/')
    
def b91():
    inputbox.insert(INSERT,'7')
def b92():
    inputbox.insert(INSERT,'8')
def b93():
    inputbox.insert(INSERT,'9')
def b94():
    inputbox.insert(INSERT,'+')
def b95():
    inputbox.insert(INSERT,'-')
    
def b101():
    inputbox.insert(INSERT,'0')
def b102():
    inputbox.insert(INSERT,'.')
def b103():
    inputbox.insert(INSERT,'e')
def b104():
    inputbox.insert(INSERT,'ans[]')
def b105():
    global i0
    ans.append(1)
    ans[i0]=eval(inputbox.get())
    a='ans[%d]=%s\n    ='%(i0,inputbox.get())
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1
def b1051(event):
    global i0
    ans.append(1)
    content=inputbox.get()
    content=content.split('/')
    
    string=''
    for i in range(len(content)-1):
        
        string=string+content[i]+'/1.0/'
    string=string+content[len(content)-1]
    
    
    ans[i0]=eval(string)
    a='ans[%d]=%s\n    ='%(i0,inputbox.get())
    outputbox.insert(END,a)
    outputbox.insert(END,ans[i0]) 
    outputbox.insert(END,'\n')
    i0=i0+1
def P(x,y):
    return (factorial(x)+0.0)/(factorial(x-y))
def C(x,y):
    return P(x,y)/P(y,y)
global ans
ans=[]
i0=0
kxjsq = Tk()
canvas = Canvas(kxjsq,width = 1000, height = 666)
im=PhotoImage(file='bg.gif')
im3=PhotoImage(file='3.gif')
canvas.create_image(500,333,image = im)
canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->科学计算器',font=('', 20 ,'bold'),fill='white')
canvas.create_text(220,60,text='输出框(outputbox)',font=('', 15 ,'bold'),fill='white')
outputbox=Text(kxjsq,width=50,height=25,bd=5)
outputbox.place(x=20,y=80) #输出

canvas.create_text(220,505,text='输入框(inputbox)',font=('', 15 ,'bold'),fill='white')

inputbox=Entry(kxjsq,width=15,font=('', 40),bd=5)
inputbox.place(x=20,y=520)  #输入
l10=['不定积分','定积分','微分','累加','累乘']
l1=[b11,b12,b13,b14,b15]
l20=['统计','矩阵','矩阵运算','方程','方程组']
l2=[b21,b22,b23,b24,b25]
l30=['sin','cos','tan','log(x,a)','abs']
l3=[b31,b32,b33,b34,b35]
l40=['arcsin','arccos','arctan','√','x^y']
l4=[b41,b42,b43,b44,b45]
l50=['P','C','->分数','->小数','I']
l5=[b51,b52,b53,b54,b55]
l60=['π','e','(',')','!']
l6=[b61,b62,b63,b64,b65]


l70=['1','2','3','DEL','AC']
l7=[b71,b72,b73,b74,b75]
l80=['4','5','6','*','/']
l8=[b81,b82,b83,b84,b85]
l90=['7','8','9','+','-']
l9=[b91,b92,b93,b94,b95]
l00=['0','.','*10^x','ANS','=']
l0=[b101,b102,b103,b104,b105]
for i in range(5):
     Button(kxjsq,text=l10[i],width=8,height=2,bg='pink',font=('', 10 ,'bold'),command=l1[i]).place(x=500+100*i,y=100)
     Button(kxjsq,text=l20[i],width=8,height=2,bg='pink',font=('', 10 ,'bold'),command=l2[i]).place(x=500+100*i,y=150)
     
     Button(kxjsq,text=l30[i],width=8,height=2,bg='lightgreen',font=('', 10 ,'bold'),command=l3[i]).place(x=500+100*i,y=200)
     Button(kxjsq,text=l40[i],width=8,height=2,bg='lightgreen',font=('', 10 ,'bold'),command=l4[i]).place(x=500+100*i,y=250)
     Button(kxjsq,text=l50[i],width=8,height=2,bg='lightgreen',font=('', 10 ,'bold'),command=l5[i]).place(x=500+100*i,y=300)
     Button(kxjsq,text=l60[i],width=8,height=2,bg='lightgreen',font=('', 10 ,'bold'),command=l6[i]).place(x=500+100*i,y=350)
     
     Button(kxjsq,text=l70[i],width=8,height=2,bg='lightblue',font=('', 10 ,'bold'),command=l7[i]).place(x=500+100*i,y=400)
     Button(kxjsq,text=l80[i],width=8,height=2,bg='lightblue',font=('', 10 ,'bold'),command=l8[i]).place(x=500+100*i,y=450)
     Button(kxjsq,text=l90[i],width=8,height=2,bg='lightblue',font=('', 10 ,'bold'),command=l9[i]).place(x=500+100*i,y=500)
     Button(kxjsq,text=l00[i],width=8,height=2,bg='lightblue',font=('', 10 ,'bold'),command=l0[i]).place(x=500+100*i,y=550)
c2=Button(kxjsq,image=im3,command=a2)
c2.place(x=900,y=600)
kxjsq.bind('<Return>',b1051)
inputbox.focus_set()
canvas.pack()
mainloop()

# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time
def tc():
    dwsy30.destroy()
    os.system("menu.py")
def jr():
    dwsy30.destroy()
    os.system("dwsy3.py")
    
dwsy30 = Tk()
canvas = Canvas(dwsy30,width = 656, height = 490)
im=PhotoImage(file='dwsy30.gif')
canvas.create_image(328,245,image = im)

Button(dwsy30,width=10,height=2,text='后退',fg='red',command=tc).place(x=200,y=400)
Button(dwsy30,width=10,height=2,text='进入',fg='red',command=jr).place(x=400,y=400)
canvas.pack()
mainloop()

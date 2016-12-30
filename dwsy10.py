# -*- coding:utf-8 -*-
from Tkinter import *         # 导入Tkinter模块
import os
import time
def tc():
    dwsy10.destroy()
    os.system("menu.py")
def jr():
    dwsy10.destroy()
    os.system("dwsy1.py")
    
dwsy10 = Tk()
canvas = Canvas(dwsy10,width = 656, height = 490)
im=PhotoImage(file='dwsy10.gif')
canvas.create_image(328,245,image = im)

Button(dwsy10,width=10,height=2,text='后退',fg='red',command=tc).place(x=200,y=400)
Button(dwsy10,width=10,height=2,text='进入',fg='red',command=jr).place(x=400,y=400)
canvas.pack()
mainloop()

#coding=utf-8
from numpy import *
import time
from matplotlib.pyplot import *
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

# calculate Euclidean distance
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))

# init centroids with random samples
def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]
    return centroids

# k-means cluster
def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    ## step 1: init centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged= False
        ## for each sample
        for i in xrange(numSamples):
            minDist  = 100000.0
            minIndex = 0
            ## for each centroid
            ## step 2: find the centroid who is closest
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist=distance
                    minIndex = j
            
            ## step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2

        ## step 4: update centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis = 0)

    print 'Congratulations, cluster complete!'
    return centroids, clusterAssment

# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
    figure(figsize=(7,4))
        
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1
    # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    
    for i in range(k):
        plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

    savefig('kmeans.jpg')
    image= Image.open("kmeans.jpg")
    pic=ImageTk.PhotoImage(image)
    canvas.create_image(500,310,image=pic)
    canvas.pack()
    mainloop()

    
def cal():
## step 1: load data
    print "step 1: load data..."
    dataSet = []
    #fileIn = open('test.txt')
    
    #for line in fileIn.readlines():
   #             lineArr = line.strip().split('\t')
   #             dataSet.append([float(lineArr[0]), float(lineArr[1])])
  
    csvfile=open(filetext.get(),'r')  
    i=0
    a=[]
    b=[]
    aa=[]
    dataSet=[]
    for eachline in csvfile:
        x=eachline.split(',')
        if i==0:
            i=1
            continue
        aa.append(x)
        a.append(eval(x[0]))
        b.append(eval(x[1]))
    csvfile.close()


    dataSet = zeros((len(a),2))
    dataSet[:,0]=a

    dataSet[:,1]=b      
    csvfile.close()
## step 2: clustering...

    dataSet = mat(dataSet)
    k = eval(ktext.get())
    centroids, clusterAssment = kmeans(dataSet, k)  
## step 3: show the result  
 
    showCluster(dataSet, k, centroids, clusterAssment)

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

canvas.create_text(500,20,text='基于Python的专业辅助计算系统-->k均值聚类（k-means）',font=('', 20 ,'bold'),fill='green')
#canvas.create_text(500,70,text='主成分分析：k均值聚类（k-means）',font=('', 20 ,'bold'),fill='green')
canvas.create_text(225,545,text='文件路径：',font=('', 18 ,'bold'),fill='yellow')
canvas.create_text(340,595,text='K=',font=('', 18 ,'bold'),fill='yellow')

i=170
j=300


ktext=Entry(root,font=('', 20 ,'bold'),width=5,bd=1)
ktext.place(x=200+i,y=190+j+90)
ktext.insert(END,'4')
filetext=Entry(root,font=('', 20 ,'bold'),width=28,bd=1)
filetext.place(x=110+i,y=230+j)

filetext.insert(END,'kmeans.csv')
Button(root,text='计算',command=cal,font=('', 15 ,'bold'),bg='orange',width=10).place(x=430+i,y=280+j)
Button(root,text='选择文件',command=choosefile,font=('', 15 ,'bold'),bg='orange').place(x=550+i,y=230+j)



canvas.pack()
root.mainloop()





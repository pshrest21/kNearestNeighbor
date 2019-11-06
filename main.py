#Spirit Animal: ApricotZebra
#Date: 11/04/2019
#Challenge Number: 4

import numpy as np
import math
import matplotlib.pyplot as mplot

kValue=input("Enter the value of k (should be a positive integer)")
try:
    kValue=np.float64(kValue)
    kValue=int(kValue)
    if kValue>0:
        file1=open("us_outline.csv","r")
        file2=open("data.csv","r")
        
        data1=file1.read()
        data1=data1.split("\n")
        
        data2=file2.read()
        data2=data2.split("\n")
        
        xaxis=[]
        yaxis=[]
        x1=[]
        y1=[]
        myList=[]
        values=[]
        x=[]
        y=[]
        v=[]
        coordinate=[]
        
        def dist(a,b):    
            return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
            
        
        for i in range(0, len(data1)):
            data1[i]=data1[i].split(", ")
            data1[i][0]=np.float64(data1[i][0])
            data1[i][1]=np.float64(data1[i][1])
            
            x1.append(data1[i][0])
            y1.append(data1[i][1])
            
        for i in range(0, len(data2)):
            data2[i]=data2[i].split(",")
            
            data2[i][0]=np.float64(data2[i][0])
            data2[i][1]=np.float64(data2[i][1])
            data2[i][2]=np.float64(data2[i][2])
            
            points=(data2[i][0], data2[i][1])
            coordinate.append(points)
            
            xaxis.append(data2[i][0])
            yaxis.append(data2[i][1])
            values.append(data2[i][2])
        
        for i in range(0, 194):
            for j in range(0, 120):
                myList=[]
                sum=0
                average=0
                x.append(i)
                y.append(j)
                m=0
                for k in coordinate:
                    distance=dist((i,j),(k))
                    myList.append([distance, values[m]])
                    m+=1
                myList=sorted(myList)     
                
                for l in range(0,kValue):
                    sum=sum+myList[l][1]
                average=sum/kValue
                v.append(average)
                      
        mplot.scatter(x, y,marker='s', c=v, cmap="viridis")
        mplot.plot(x1, y1, color='k')
        mplot.show()
    else:
        print("Please enter a positive integer")
except:
    print("Please enter a positive integer")  
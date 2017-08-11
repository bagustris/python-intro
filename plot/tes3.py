import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()
fig=plt.figure()
plt.axis([0,100,0,1])


i=0
x=list()
y=list()

while i <100:
    temp_y=np.random.random()
    x.append(i)
    y.append(temp_y)
    plt.scatter(i,temp_y)
    i+=1
    plt.show()
    plt.pause(0.01) #Note this correction
    #plt.show()
    

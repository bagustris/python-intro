import matplotlib.pyplot as plt
import numpy as np
import time

fig=plt.figure()
plt.axis([0,100,0,1])
plt.ion                 #animation


for i in range(100):
    y = np.random.random()
    plt.scatter(i, y)
    plt.draw()
    time.sleep(0.05)

plt.show()

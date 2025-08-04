'''# display the multipale plots - with subplot() you can draw multiple plots inone  figure.
import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3,])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)# the figure has 1 row, 2 colums and this plot is the 1 plot.
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()


# now we will draw 2 plot on top of each other
import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3,])
y = np.array([3,8,1,10])
plt.subplot(2,1,1)# the figure has 1 row, 2 colums and this plot is the 1 plot.
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()'''


# now we will draw a challange of 6 plot 
import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3,])
y = np.array([3,8,1,10])
plt.subplot(2,3,1)# the figure has 1 row, 2 colums and this plot is the 1 plot.
plt.title('plot1')
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.title('plot2')
plt.plot(x,y)

#plot3
x = np.array([0,1,2,3,])
y = np.array([3,8,1,10])
plt.subplot(2,3,3)# the figure has 1 row, 2 colums and this plot is the 1 plot.
plt.title('plot3')
plt.plot(x,y)

#plot4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.title('plot4')
plt.plot(x,y)

#plot5
x = np.array([0,1,2,3,])
y = np.array([3,8,1,10])
plt.subplot(2,3,5)# the figure has 1 row, 2 colums and this plot is the 1 plot.
plt.title('plot5')
plt.plot(x,y)

#plot6
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,6)
plt.title('plot6')
plt.plot(x,y)

plt.suptitle('my plot')
plt.show()

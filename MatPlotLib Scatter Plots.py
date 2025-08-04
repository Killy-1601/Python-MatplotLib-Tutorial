'''# scatter - the scatter() function one dot for each obsevation.
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)
plt.show()'''


# now we wil compare 2 plot on ame figure
import matplotlib.pyplot as plt
import numpy as np

# day 1, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)

# day 2 , the age and speed
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,22,])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,80,85,91])
plt.scatter(x,y)
plt.show()
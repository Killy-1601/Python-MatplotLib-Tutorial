# linestyle or ls - is used to change the style of the plotted line 
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,linestyle = ':')
plt.show()


# line color - c
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,c = 'r')
plt.show()


# line width - lw  width of a line
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,lw = '25.5')
plt.show()


# example for maltipale line
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([3,8,1,10])
ypoints = np.array([6,2,7,11])
plt.plot(xpoints,ypoints,lw = '25.5')
plt.show()


# example for maltipale line
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([3,8,1,10])
ypoints = np.array([6,2,7,11])
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()


# you can use argument to emphasize each point with specified marker
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker ='o')
plt.show()


# format strings "fnt" - marker|line|color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,'o-r')
plt.show()


# marker size
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,marker = 'o',ms = 50 ,mec = 'r')
plt.show()


# marker face color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,marker = 'o',ms = 50 ,mfc = 'r' ,mec = 'g')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
size=3
img_1=np.random.randint(0,2,(size,size))
img_1   #fake image, you should read from a file
plt.imshow(img_1,cmap='Greys',interpolation='nearest')
plt.show()

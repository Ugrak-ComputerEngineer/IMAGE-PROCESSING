import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread("plaka.jpg")
img_5=np.zeros((img_1.shape [0:2]))
img_2=img_1

#plt.imshow(img_6,plt.cm.binary)
#plt.show()

threshold=150
for i in range(img_2.shape[0]): 
    for j in range(img_2.shape[1]):
        n=img_2[i,j,0]/3+img_2[i,j,1]/3+img_2[i,j,2]/3
        #img_3[i,j]=n
        if n>threshold:
            img_5[i,j]=255
        else:
            img_5[i,j]=0
plt.subplot(1,2,1),plt.imshow(img_2)
plt.subplot(1,2,2),plt.imshow(img_5,plt.cm.binary)
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import scipy

img_1 = plt.imread(r'C:\Users\BM\Desktop\1.jpg')

def convert(RGB_Pixel):
    return RGB_Pixel[0]/3 + RGB_Pixel[1]/3 + RGB_Pixel[2]/3

# convert([2,5,7])

img_2 = np.zeros((img_1.shape[0],img_1.shape[1]))        # aynı boyutta olustur

for i in range (img_1.shape[0]):
    for j in range (img_2.shape[1]):
        img_2[i,j] = convert(img_1[i,j,:])

plt.subplot(1,2,1)                                        # subplot resimleri yan yana göstermek için
plt.imshow(img_1)
plt.subplot(1,2,2)
plt.imshow(img_2,cmap = 'gray')
plt.show()


#------------------------------------------
#fonksiyonun düzenli hali

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
def  convertRGB_to_GrayLevel(image_1):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range (img_1.shape[0]):
        for j in range (img_1.shape[1]):
            img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3
    imsave(image_1+"_gray.jpg",img_2)
    plt.subplot(1,2,1) #renkli fotoğrafı siyah-beyaz yani gray seviyeye dönüştürdük.
    plt.imshow(img_1)
    plt.subplot(1,2,2)
    plt.imshow(img_2,cmap='gray')
    plt.show()
convertRGB_to_GrayLevel(r'C:\Users\ugur\Desktop\test_10.jpg')


-------------------------------------
iki resimdeki farkları bulma

import matplotlib.pyplot as plt

img_1 = plt.imread(r'C:\Users\BM\Desktop\var.jpg')
img_2 = plt.imread(r'C:\Users\BM\Desktop\yok.jpg')
plt.imshow(img_2-img_1)
plt.show()


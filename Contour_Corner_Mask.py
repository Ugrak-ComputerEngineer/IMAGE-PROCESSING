#---İNTERNAL da çizgi dışı 0 lar var içerde ise 1 var. EXTERNAL da ise çizgi içi 0 dışında 1 ler var.---#


import numpy as np
import matplotlib.pyplot as plt
size=3
img_1=np.random.randint(0,2,(size,size))


#------------------------------#
#---Verilen resimde mask yani belli ölçekli matrisel olarak resmi dolaşması (Contour Corner Mask) için yazılan fonksiyon---#

def count_mask(image,mask):
    # input :
    #image m*n black-white image
    #mask 2*2 mask
    counter=0
    m,n=image.shape
    for i in range (m-1):
        for j in range(n-1):
            a=b=c=d=False
            if (image[i,j]==mask[0][0]):
                a=True
            if(image[i,j+1]==mask[0][1]):
                b=True
            if(image[i+1,j]==mask[1][0]):
                c=True
            if(image[i+1,j+1]==mask[1][1]):
                d=True
            if(a and b and c and d):
                counter=counter+1
    return counter
 
 
#-------------------------#
#---Corner noktaları matrisler olarak verildi.---#

i_m_1=[[1,0],[0,0]]
i_m_2=[[0,1],[0,0]]
i_m_3=[[0,0],[1,0]]
i_m_4=[[0,0],[0,1]]
e_m_1=[[0,1],[1,1]]
e_m_2=[[1,0],[1,1]]
e_m_3=[[1,1],[0,1]]
e_m_4=[[1,1],[1,0]]
i_m_l=[i_m_1,i_m_2,i_m_3,i_m_4]
e_m_l=[e_m_1,e_m_2,e_m_3,e_m_4]


#--------------------------------#
#---Resmin belli bir bölgesine uygulanan mask'ın matrisel olarak 1 ve 0 larını yani internal,external noktalarını bulan fonksiyon---#

def count_internal_mask(image):
    counter_internal=0 
    for mask in i_m_l:
        counter_internal=counter_internal+count_mask(img_1,mask)
    return counter_internal
def count_external_mask(image):
    counter_external=0 
    for mask in e_m_l:
        counter_external=counter_external+count_mask(img_1,mask)
    return counter_external
    
c_1=count_internal_mask(img_1)
c_2=count_external_mask(img_1)
c_1,c_2   

img_1   #fake image, you should read from a file
plt.imshow(img_1,cmap='Greys',interpolation='nearest')
plt.show()    
 
    
    
    
    
    
    
    
    
    
    
    
    
    

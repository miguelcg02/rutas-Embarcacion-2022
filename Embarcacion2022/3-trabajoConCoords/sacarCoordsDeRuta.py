import cv2
import numpy as np

img1 = cv2.imread('2RiosEnguatape/sacarCoords/magangue_pinillosRojo.png')

img2 = cv2.imread('2RiosEnguatape/sacarCoords/puertoNare_puertoTriunfoRojo.png') #Rio

img3 = cv2.imread('2RiosEnGuatape/sacarCoords/PuertoBerrioPuertoNareRojo.png')

def sacarCords(lonMin,lonMax,latMin,latMax,img): 
    
    longi = lonMax-lonMin #X
    lati = latMax-latMin #Y
    
    # print(longi)
    # print(lati)

    largo = len(img[0]) #X
    # print(largo)

    alto = len(img) #Y
    # print(alto)

    aumX = longi/largo
    # print(aumX)
    aumY = lati/alto
    # print(aumY)

    _array = []
    
    for i in range(alto):
        for j in range(largo):
            if(img[i][j][2] == 255):        
                a = latMax-(aumY*i)
                b = lonMin+(aumX*j)
                temp = [a,b]
                _array.append(temp)
    
    np.savetxt('test.txt', _array,fmt='%s')

sacarCords(-74.7879,-74.3929,8.8622,9.2953,img1)
# sacarCords(-74.6743,-74.5284,5.8839,6.2484,img2)
# sacarCords(-74.6369,-74.3475,6.1495,6.5239,img3)


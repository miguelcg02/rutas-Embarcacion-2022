import cv2
import imutils

img1 = cv2.imread('2RiosEnguatape/magangue_pinillos.png') #Guatape o magangue
img2 = cv2.imread('2RiosEnguatape/PuertoBerrioPuertoNareRojo.png') #Rio
img3 = cv2.imread('2RiosEnguatape/h.png') 
img4 = cv2.imread('2RiosEnguatape/puertoNare_puertoTriunfoRojo.png') 
img5 = cv2.imread('2RiosEnguatape/cuerpoDeAguaRepresaRedimensionada.png')

def funcion1(img1, img2,reflejarlo=False,traslacionH=0,traslacionV=0,angulo=0): #img1 la base img2 el que se le pega encima, trslacoinH (negativos para mover pX a la izq y abajo y positivos para derecha y arriba)
    if(reflejarlo==True):
        img2 = cv2.flip(img2, 0)
    
    img2 = imutils.rotate_bound(img2, angulo)

    if (len(img1)>=len(img2)):
        rows = len(img1)
    else:
        rows = len(img2)

    if (len(img1[0])>=len(img2[0])): 
        columns = len(img1[0])
    else:
        columns = len(img2[0])

    if (rows>columns):
        lado = rows
    else:
        lado = columns

    lado = int(lado)
    lado = int(lado) + int(lado/4)

    import numpy as np
    blank_image = np.zeros((lado,lado,3), np.uint8)

    comienzaHorizontal = (lado/2)-(len(img1)/2) #
    terminaHorizontal = (lado/2)+(len(img1)/2) #
    comienzaVertical = (lado/2)-(len(img1[0])/2) #
    terminaVertical = (lado/2)+(len(img1[0])/2) #

    comienzaHorizontal = int(comienzaHorizontal)
    comienzaVertical = int(comienzaVertical)
    terminaHorizontal = int(terminaHorizontal)
    terminaVertical = int(terminaVertical)

    for i in range(terminaHorizontal-comienzaHorizontal):
        for j in range(terminaVertical-comienzaVertical):
            blank_image[i+comienzaHorizontal][j+comienzaVertical] = img1[i][j]

    comienzaHorizontal = (lado/2)-(len(img2)/2) - traslacionV
    #terminaHorizontal = (lado/2)+(len(img2)/2) - traslacionH
    comienzaVertical = (lado/2)-(len(img2[0])/2) +  traslacionH
    #terminaVertical = (lado/2)+(len(img2[0])/2) - traslacionV

    comienzaHorizontal = int(comienzaHorizontal)
    comienzaVertical = int(comienzaVertical)
    #terminaHorizontal = int(terminaHorizontal)
    #terminaVertical = int(terminaVertical)

    for i in range(len(img2)):
        for j in range(len(img2[0])):
            if(img2[i][j][0] == 0 and img2[i][j][1] == 0 and img2[i][j][2] == 0):
                continue
            blank_image[comienzaHorizontal+i][comienzaVertical+j] = img2[i][j]

    cv2.imwrite('2RiosEnGuatape/h.png', blank_image)

    return blank_image
    
def funcion2(img):
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0):
                img[i][j] = [255,255,255]
    
    cv2.imwrite('2RiosEnGuatape/finalblanco.png', img)
                
#funcion1(img1, img2,True,-800,-570,-5)
#funcion1(img1, img4,False,-500,-600,-53)
#funcion1(img5,img4)
funcion2(img3)


# img2 = imutils.rotate_bound(img2, 32)
# cv2.imshow("a",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#cv2.imwrite('2RiosEnGuatape/a.png', blank_image)


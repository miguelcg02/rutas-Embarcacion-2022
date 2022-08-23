from skimage.morphology import skeletonize
from skimage.util import invert
import cv2

#Convert the image to a binary image

#read image
original_img = cv2.imread('./imagenMetodologia.png')  #Path of the image to read
 
# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128
 
# assign blue channel to zeros
img_binary = cv2.threshold(original_img, thresh, 255, cv2.THRESH_BINARY)[1]


#-----------------------------------

# Invert the horse image
image_invert = invert(img_binary)
# perform skeletonization
skeleton_img = skeletonize(image_invert)

# display results
cv2.imwrite('./MetodologiaEjemplos/skMetodologia.png', skeleton_img) #Path where you want to save the skeletonize of the imaga


#------------------------------------
# Now we can make a superposicion of the 2 images to see the diferrences 

rows = len(original_img)
colums = len(original_img[0])


for i in range(rows):
    for j in range(colums):
        if(skeleton_img[i][j][1] == 255):
            original_img[i][j] = [0, 255, 0]
        

cv2.imwrite('./MetodologiaEjemplos/superposicionMetodologia.png', original_img) # Path where you want to save the superposicion of the imaga
import cv2


# original_img = cv2.imread('./skMetodologia.png')  #Path of the image to read



# rows = len(original_img)
# colums = len(original_img[0])


# for i in range(rows):
#     for j in range(colums):
        
#         if(original_img[i][j][1] == 0 and original_img[i][j][0] == 0 and original_img[i][j][2] == 0):
#             original_img[i][j] = [255, 255, 255]
#         else:
#             original_img[i][j] = [255, 0, 0]
        

# cv2.imwrite('./skMetodologia3.png', original_img)



original_img = cv2.imread('./Magangue_PinillosSKGrueso2.png')
dest = cv2.imread('./Magangue_Pinillos.png')



rows = len(original_img)
colums = len(original_img[0])


for i in range(rows):
    for j in range(colums):
        if(original_img[i][j][0] == 255 and original_img[i][j][1] == 0 and original_img[i][j][2] == 0):
            dest[i][j] = [255,0,0]
        elif(not (original_img[i][j][0] == 255 and original_img[i][j][1] == 255 and original_img[i][j][2] == 255)):
            dest[i][j] = [0,0,255]
        
            
cv2.imwrite('./Magangue_Pinillos_Ruta.png', dest)
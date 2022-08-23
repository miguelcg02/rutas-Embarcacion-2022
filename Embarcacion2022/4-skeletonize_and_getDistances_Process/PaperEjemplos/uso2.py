import cv2
import numpy as np

# Create test image

mask = cv2.imread('./finalNegroNpTMP.png')  #Path of the image to read

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilate = cv2.dilate(mask, kernel, iterations=6)

# rows = len(dilate)
# colums = len(dilate[0])


# for i in range(rows):
#     for j in range(colums):
        
#         if(dilate[i][j][0] == 255):
#             dilate[i][j] = [255, 0, 0]
#         else:
#             dilate[i][j] = [255, 255, 255]

cv2.imwrite('./finalNegroNpTMP6.png', dilate)



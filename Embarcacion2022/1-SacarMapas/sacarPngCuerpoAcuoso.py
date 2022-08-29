import osmnx as ox
import matplotlib.pyplot as plt
import geopy.distance
import cv2

# Establecer coordenadas
north = 6.5053
south = 6.1673
west = -74.6046
east = -74.3321

# Sacar tag y bbox de OX
tags = {'water': 'river'}
agua = ox.geometries_from_bbox(north,south,east,west,tags)
# Plot Agua
agua.plot(facecolor='blue')

#Preprocesar imagen
plt.xlim(west,east)
plt.ylim(south,north)
plt.axis('off')

# Medidas norte sur
coords_1 = (north,west)
coords_2 = (south,west) 

# Medidas oeste - este
coords_3 = (north,west)
coords_4 = (north,east) 

# Sacara las distancias norte sur y oeste este
nor_sur = geopy.distance.geodesic(coords_1, coords_2).km
oes_est = geopy.distance.geodesic(coords_3, coords_4).km

# Guardar plot limpio
plt.savefig('1-Organizado/1-SacarMapas/1-imgOSM/nareeee.png', bbox_inches='tight',pad_inches = 0)

#Abrir imagen con cv2
img1 = cv2.imread('1-Organizado/1-SacarMapas/1-imgOSM/nareeee.png') 


# Se instancian las variables para el nuevo alto y ancho al redimencionar
pixelAlto = (nor_sur/0.00854) #Se divide por la medida en kilometros que quiere que sean los nuevos pixeles, en este caso c/ pixel medirá 0.00854 km -> 8.54m
pixelAncho = (oes_est/0.00854)

# Se le saca el promedio para la proporcion de aumento del resize
proporcion = ((pixelAlto/len(img1))+(pixelAncho/len(img1[0])))/2 

#Redondear nueva cantidad de pixeles
nueAlt = round(proporcion*len(img1))
nueAnch= round(proporcion*len(img1[0]))

# Resize
imagenFinal = cv2.resize(img1, (nueAnch,nueAlt))

# Guardado de la imagen con cv2
cv2.imwrite('1-Organizado/1-SacarMapas/2-imgEditada/nareeeeFinal.png',imagenFinal) 

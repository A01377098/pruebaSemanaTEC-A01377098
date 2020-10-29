import cv2 
import numpy as np

imagen = cv2.imread("imagen.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

print (imagen.shape)
print (imagen[0]) 

imagen = cv2.resize(imagen, (256, 256))
cv2.imwrite("resizeimagen.jpg", imagen)
#cv2.imshow("image", imagen)

imagen = cv2.imread("imagen.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
print (imagen.shape)
print (imagen[0][0]) 

imagen[0][0] = 0
imagen[0][1] = 0
imagen[0][2] = 0

cv2.imwrite("grayimagen.jpg", imagen)

Matriz = np.zeros((256, 256), np.float32)
imagen = cv2.cvtColor(Matriz, cv2.COLOR_GRAY2BGR)
print (imagen.shape)



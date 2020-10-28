#Función que calcula la matriz resultante "C" después de aplicar la operación convolución de A*B
import numpy as np

def convolucion (A, B):
   C = 0
   return C
 
Matriz1 = [[6, 9, 0, 3], [8, 4, 9, 1], [4, 1, 3, 12], [3, 2, 1, 100]]
Filtro = [[1, 0, 2], [5, 0, 9], [6, 2, 1]]

A = np.array(Matriz1)
B = np.array(Filtro)

C = np.zeros((2,2))

print (A)
print (A[1][0])
print (C)

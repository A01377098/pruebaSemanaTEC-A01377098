#Función que calcula la matriz resultante "C" después de aplicar la operación convolución de A*B=
# EJERCICIO 28 DE OCTUBRE 
# Eva Denisse Vargas Sosa A01377098

import numpy as np
def convolucion (A, B):
    contaFil = 0
    contaCol = 0
    limiteFil = len(A)
    limiteCol = len(A)
    longitudB = len(B)
    for x in range (len(C)):
        for y in range (len(C)):
            for n in range (contaFil, len(B)+contaFil):
                if len(B)+contaFil > limiteFil:
                    break
                for o in range (contaCol, len(B)+contaCol):
                    if len(B)+contaCol> limiteCol:
                        break 
                    C[x][y] += A[n][o] * B[n-contaFil][o-contaCol]
                    
            if contaCol+longitudB<limiteCol:
                contaCol += 1
            elif contaCol+longitudB== limiteCol:
                contaCol = 0
                if contaFil+longitudB< limiteFil:
                    contaFil  += 1
                elif contaFil+longitudB == limiteFil:
                    return 

Matriz = [[6, 9, 0, 3], [8, 4, 9, 1], [4, 1, 3, 12], [3, 2, 1, 100]]
Filtro = [[1, 0, 2], [5, 0, 9], [6, 2, 1]]

A = np.array(Matriz)
B = np.array(Filtro)

C = np.zeros((2,2))

convolucion(A,B)
print (C)

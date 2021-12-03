#Import random
import random

side = random.randint(2,10)

#Create the function below:
def matrixBuilder(matrix_size):
    matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(1)
        matrix.append(row)
    return matrix

print(matrixBuilder(side))
#import numpy as np

#from typing import List
#from bitarray import bitarray

  # Размерность битсета

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
def gauss(matrix, vector):
    n = len(matrix)
    # matrix = transpose_matrix(matrix)
    for i in range(n):
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        for k in range(i + 1, n):
            c = -matrix[k][i]
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] = (matrix[k][j]+ c * matrix[i][j])%2
            vector[k] = (vector[k]+ c * vector[i])%2

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = vector[i]
        for k in range(i - 1, -1, -1):
            vector[k] = (vector[k] - matrix[k][i] * x[i])%2
    ans=[]
    for i in range(M):
        ans.append(x[i])
    return ans
# Определение операции сложения по модулю 2

N=30
M=13
#richagi = ([ [0,3,5], [7,8,19,5],[1,4,8,10,11,12],[2,5,7,9,13,17],[10,12,15,18,19,17], [18,12, 11], [6,7,8,9,10], [2,8,9,12,15,16,17],[1,19,18,17],[3,5,8,10,14]] )
richagi = [[0,3,5,19], [7,8,19,5,14,20],[1,4,8,10,11,12,13,29],[2,5,7,9,13,17],[10,12,15,18,19,17], [18,12, 11,15,17,19,20], [6,7,8,9,10], [2,8,9,12,15,16,17],[1,19,18,17],[3,5,8,10,14], [0,1,3,17,19,20,21,22], [2,3,5,7,9,11,13], [0,7,13,15,16,19,25,27,29]]
A=[]
for i in range(M):
    arr=[]
    for j in range(N):
        if j in richagi[i]:
            arr.append(1)
        else:
            arr.append(0)
    A.append(arr.copy())


#start = [1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0]
start = [1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0, 1, 1, 1,0,0,1,0,1,0,1]
finish = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b=[]
for i in range(N):
    b.append((finish[i] - start[i])%2)


# Решение системы уравнений над полем вычетов по модулю 2
for i in range(M,N):
    A.append(finish.copy())
A=transpose_matrix(A)
#print(A)
res = gauss(A, b)
print(res)

def LU_decomposition(matrix):
    """
    LU Decomposition by Crout's method
    """
    k = len(matrix)
    L = [[0 for i in range(k)] for j in range(k)]
    U = [[0 for i in range(k)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            if i == j:
                U[i][j] = 1
            else:
                U[i][j] = 0
    

    for i in range(k):
        for j in range(i+1):
            sum = 0
            for p in range(j):
                sum += L[i][p] * U[p][j]
            L[i][j] = matrix[i][j] - sum
        for j in range(i+1, k):
            sum = 0
            for p in range(i):
                sum += L[i][p] * U[p][j]
            U[i][j] = (matrix[i][j] - sum) / L[i][i]
    return L, U


def LU_equation_solver(matrix):

    L, U = LU_decomposition(matrix)
    k = len(matrix)
    y = [0 for i in range(k)]
    x = [0 for i in range(k)]

    for i in range(k):
        sum = 0
        for p in range(i):
            sum += L[i][p] * y[p]
        y[i] = (matrix[i][k] - sum) / L[i][i]

    for i in range(k-1, -1, -1):
        sum = 0
        for p in range(i+1, k):
            sum += U[i][p] * x[p]
        x[i] = (y[i] - sum) / U[i][i]

    return x, y
    
matrix = [[1,-2,7,2,-18], [2,5,-3,1,31],[9,-6,4,1,35],[4,-3,-6,7,15]]

L, U = LU_decomposition(matrix)
print("L:")
print(L)
print("U:")
print(U)

print("LU Equation Solver:")
x, y = LU_equation_solver(matrix)
print("x:")
print(x)
print("y:")
print(y)


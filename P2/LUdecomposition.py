def doolittle(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for i in range(n):
        L[i][i] = 1.0
        for j in range(i, n):
            soma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - soma
        for j in range(i+1, n):
            soma = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - soma) / U[i][i]

    return L, U
    

matrix = [[2,1,1], [-1,-1,-1], [6,-2,4]]
b = [3,-1,14]
# matrix = [[2,3,4], [1,1,1], [4,-1,-2]]
# b = [20,6,-4]


def LU_equation_solver(matrix, b):
    """
    param: matrix: matrix to be solved
    param: b: vector to be solved
    return: x: solution of the system of equations
    """

    L, U = doolittle(matrix)
    k = len(matrix)
    y = [0 for i in range(k)]
    x = [0 for i in range(k)]


    # solve Ly = b
    for i in range(k):
        sum = 0
        for p in range(i):
            sum += L[i][p] * y[p]
        y[i] = (b[i] - sum) / L[i][i]

    # solve Ux = y
    for i in range(k-1, -1, -1):
        sum = 0
        for p in range(i+1, k):
            sum += U[i][p] * x[p]
        x[i] = (y[i] - sum) / U[i][i]



    return x, y

print(LU_equation_solver(matrix,b))
print(doolittle(matrix))

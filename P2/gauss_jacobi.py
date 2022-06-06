def gauss_jacobi(A, b, X, tol=1e-5):
    """
    Função que resolve o sistema Ax = b usando o método de Gauss-Jacobi
    :param A: matriz do sistema
    :param b: vetor da direita
    :param X: vetor de solução
    :return: vetor de solução
    """
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i != j:
                A[i][j] /= A[i][i]
        b[i] /= A[i][i]
        A[i][i] = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                b[i] -= A[i][j]*X[j]
    for i in range(n):
        X[i] = b[i]
    return X

matrix = [[3,-1,-1], [1,3,1], [2,-2,4]]
vector = [1,5,4]
x0 = [0,0,0]

print(gauss_jacobi(matrix, vector, x0))
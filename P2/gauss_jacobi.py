def gauss_jacobi(A, b, x0, tol=1e-5):
    """
    Função que resolve o sistema Ax = b usando o método de Gauss-Jacobi
    :param A: matriz do sistema
    :param b: vetor da direita
    :param X: vetor de solução
    :return: vetor de solução
    """
    n = len(A)

    desvio = 1

    X = [0] * n
    k = 0
    while(desvio > tol):
        for i in range(n):
            soma = 0
            for j in range(n):
                if(i != j):
                    soma += A[i][j] * X[j]
            X[i] = (b[i] - soma) / A[i][i]

        desvio = 0
        for i in range(n):
            desvio += abs(X[i] - x0[i])
        x0 = X[:]
        k += 1

    return X, k

matrix = [[3,-1,-1], [1,3,1], [2,-2,4]]
vector = [1,5,4]
x0 = [0,0,0]

print(gauss_jacobi(matrix, vector, x0))
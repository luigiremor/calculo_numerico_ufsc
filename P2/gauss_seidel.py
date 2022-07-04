def gauss_seidel(A, b, x0, tol, w):
    """
    param: A: matrix to be solved
    param: b: vector to be solved
    param: x0: initial guess
    param: tol: tolerance
    param: w: relaxation parameter
    return: x: solution of the system of equations
    return: k: number of iterations
    """
    n = len(A)
    x = [0] * n

    k = 0
    desvio = 1

    # seidel method with relaxation parameter w 
    while(desvio > tol):
        for i in range(n):
            soma = 0
            for j in range(n):
                if(i != j):
                    soma += A[i][j] * x[j]
            # x[i] = (b[i] - soma) / A[i][i]
            # x[i] = x[i] + w * (x0[i] - x[i])
            x[i] = (1-w) * x[i] + w * (b[i] - soma) / A[i][i]
        desvio = 0
        for i in range(n):
            desvio += abs(x[i] - x0[i])
        x0 = x[:]
        k += 1
    
    return x, k, desvio

A = [[5,2,1],[-1,4,2], [2,-3,10]]
b = [7,3,-1]

x0=[0,0,0]

tol = 1e-6

w = 0.95

print(gauss_seidel(A,b,x0, tol, w))
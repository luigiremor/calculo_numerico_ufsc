def gauss(A,b):

    ca = A.copy()
    cb = b

    n = len(b)

    o = [i for i in range(n)] 

    for k in range(n-1):
        # procurando o maior em modulo
        maior = abs(A[o[k]][k])
        p = k
        for i in range(k+1, n):
            if abs(A[o[i]][k]) > maior:
                maior = abs(A[o[i]][k])
                p = i

        # trocando as linhas apenas no vetor de ordenamento
        if p > k:
            aux = o[k]
            o[k] = o[p]
            o[p] = aux

        # triangularizando
        for i in range(k+1, n):
            m = A[o[i]][k] / A[o[k]][k]
            for j in range(k, n):
                A[o[i]][j] -= m * A[o[k]][j]
            b[o[i]] -= m * b[o[k]]

    # retrosubstituição
    x = [(b[o[n]] / A[o[n]][n]) for n in range(n)]

    for i in range(n-1, -1, -1):
        x[i] = (b[o[i]] - sum(A[o[i]][j] * x[j] for j in range(i+1, n))) / A[o[i]][i]

    # resíduos
    # transposta de x
    xt = [x[i] for i in range(n)]

    # transposta de cb
    bt = [b[i] for i in range(n)]

    # resíduos
    r = [abs(bt[i] - sum(ca[i][j] * xt[j] for j in range(n))) for i in range(n)]




    return ca, cb, x, o, r

A =[[1, 1, 1.5, 1, 1.5, 0, 0, 0, 0, 0],
    [0, 1, 0.01, 0.51, 1.5, 0.5, 0, 0, 0, 0],
    [2.9, 1, 2, 1, 1, 0, 5, 0, 0, 0,],
    [9, 1, 0.2, 1, 1, 0, 0, 1.5, 0, 0],
    [1, 0, 2, 0, 0, 1, 1, 1, 0, 2],
    [0, 1, 0, 0, -2, 0, 1, -1, 1, 1] ,
    [1, 0, 2, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 2, 0, 1, 1, 1, -1],
    [0, 0, 1, 0, 2, 1, -1, 0, -1, -1],
    [0, 1, 0, 0, 2, 0, 1, 0, 1, 1]]

b = [4, -3, 1, -1, -1, 0, -1, 1, 3, -2]

ca, cb, x, o, r = gauss(A,b)

print("\nMatriz A:")
for i in range(len(A)):
    print(A[i])

print("\nVetor b:")
print(b)

print('Vetor x:')
print(x)

print('Vetor o:')
print(o)

print('Vetor r:')
print(r)


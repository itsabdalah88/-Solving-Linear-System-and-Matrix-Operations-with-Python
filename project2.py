import sympy as s

A = s.Matrix([
    [6,4,-8,9,7,6,5],
    [7,8,6,-5,4,7,8],
    [4,0,7,8,9,7,6],
    [5,6,4,5,7,8,7],
    [5,4,-2,-5,7,3,-2],
    [4,5,7,8,9,7,6],
    [3,2,4,5,7,8,6]
])

B = s.Matrix([
    [1,2,3,4,5,6,7,8],
    [2,4,6,8,10,12,14,16],
    [3,6,9,12,15,18,21,24],
    [4,8,12,16,20,24,28,32],
    [5,10,15,20,25,30,35,40],
    [6,12,18,24,30,36,42,48],
    [7,14,21,28,35,42,49,56],
    [8,16,24,32,40,48,56,64]
])

for M in [A, B]:
    print("Transpose:")
    print(M.T)
    print("Determinant:")
    det = M.det()
    print(det)
    if det == 0:
        print("The matrix is singular, so it does not have an inverse")
    else:
        print("Inverse:")
        print(M.inv())
    print("Adjoint:")
    print(M.adjugate())
    print("Cofactor Matrix:")
    print(M.cofactor_matrix())
    print("Minors:")
    print(M.minor_submatrix(0,0))
    print("-----------------------------")
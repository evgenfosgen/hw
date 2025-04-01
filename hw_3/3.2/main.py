from matrix import Matrix

A = Matrix.random_matrix(0, 10, (10, 10), seed=0)
B = Matrix.random_matrix(0, 10, (10, 10), seed=0)


C_plus = A + B
C_plus.to_file("matrix+.txt")
print("сложение:\n" + str(C_plus))


C_um = A * B
C_um.to_file("matrix*.txt")
print("покомпонентное умножение:\n" + str(C_um))

C_mat_um = A @ B
C_mat_um.to_file("matrix@.txt")
print("матричное умножение:\n" + str(C_mat_um))


# python3 main.py

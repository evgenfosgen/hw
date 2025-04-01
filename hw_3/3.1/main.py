from matrix import Matrix


A = Matrix.random_matrix(0, 10, (10, 10), seed=0)
B = Matrix.random_matrix(0, 10, (10, 10), seed=0)


(A + B).to_file("matrix+.txt")
(A * B).to_file("matrix*.txt")
(A @ B).to_file("matrix@.txt")


# python3 main.py

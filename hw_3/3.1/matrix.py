import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.shape = self.data.shape

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError(
                "сложить можно только матрицы одинакового размера")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError(
                "перемножить покомпонентно можно только матрица одинакового размера")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError(
                "матрично перемножить можно только матрицы одинакового размера")
        return Matrix(self.data @ other.data)

    def __str__(self):
        return str(self.data)

    def to_file(self, filename):
        with open(filename, "w") as f:
            for row in self.data:
                f.write(" ".join(map(str, row)) + "\n")

    @staticmethod
    def random_matrix(low, high, shape, seed):
        np.random.seed(seed)
        return Matrix(np.random.randint(low, high, shape))

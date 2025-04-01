import numpy as np

# ПРИМеСИ


class StrMixin:
    def __str__(self):
        return "\n".join(
            " ".join(f"{item:4}" for item in row)
            for row in self.data
        )


class FileMixin:
    def to_file(self, filename):
        with open(filename, "w") as f:
            for row in self.data:
                f.write(" ".join(map(str, row)) + "\n")


class AccessorMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)
        self.shape = self._data.shape

# ОСНОВАНОЙ КЛАСС


class Matrix(StrMixin, FileMixin, AccessorMixin):
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

    @staticmethod
    def random_matrix(low, high, shape, seed):
        np.random.seed(seed)
        return Matrix(np.random.randint(low, high, shape))

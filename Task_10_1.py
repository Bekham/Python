class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ])

    def __str__(self):
        enter = ''
        for row in self.matrix:
            enter += f'{" ".join(map(str, row))}\n'
        return enter


m1 = Matrix([[10, 2, 3], [3, 4, 3], [9, 4, 67]])
m2 = Matrix([[3, 76, 23], [4, 34, 45], [76, 43, 21]])
print(f'{m1}+\n{m2}=')
print(m1 + m2)

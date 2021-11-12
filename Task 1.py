a = [[1, 2, 3, 4], [7,6,8,5], [0,9,3,2]]
b = [[6, 7, 4, 5], [8,0,3,2], [7,6,3,1]]

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join((map(str, self.matrix)))

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[0])):
                result[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, result))

matrx1 = Matrix(a)
matrx2 = Matrix(b)

print(matrx1, '\n')
print(matrx2, '\n')
print(matrx1 + matrx2)
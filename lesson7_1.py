class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(len(self.list1)):
            for x in range(len(self.list2)):
                matrix[i][x] = self.list1[i][x] + self.list2[i][x]
        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in matrix]))

    def __str__(self, matrix=None):
        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in matrix]))

my_matrix = Matrix(
            [[9, 5, 0],
            [2, 1, 9],
            [1, 1, 1]],
            [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 2]])

print(my_matrix.__add__())
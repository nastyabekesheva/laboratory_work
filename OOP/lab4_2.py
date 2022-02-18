class OverloadShift:

    def __rshift__(self, other):
        other.item = input()

    def __lshift__(self, other):
        print(other.item)

class Matrix(OverloadShift):
    def __init__(self, rows, cols):
        self.matrix = self.__getmatrix__(rows, cols)
        self.rows = rows
        self.cols = cols

    def __getmatrix__(self, rows, cols):
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        print("Enter values: ")
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(input())
        return matrix

    def __getitem__(self, item1):
        return self.matrix[item1]


if __name__ == '__main__':
    cout = OverloadShift()
    cin = OverloadShift()
    matrix = Matrix(2, 2)
    a = OverloadShift()
    a = matrix[1][1]
    cout << a

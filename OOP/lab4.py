from lab2_2 import AnyMatrix

class OverloadData(AnyMatrix):
    def __init__(self, rows, cols):
        self.matrix = self.__get__(rows, cols)
        self.rows = rows
        self.cols = cols

    def __get__(self, rows, cols):
        temp = True
        while temp:
            matrix = []
            for i in range(rows):
                matrix.append([int(j) for j in input().split()])
            size = sum(len(i) for i in matrix)
            if size != rows*cols:
                print("Incorrect input. Plese try again.")
            else:
                return matrix
                temp = False

    def __print__(self):
        for i in self.matrix:
            print(*i)


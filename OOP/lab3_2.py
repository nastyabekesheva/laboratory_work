from lab2_2 import AnyMatrix

class Overload(AnyMatrix):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = matrix.rows
        self.cols = matrix.cols

    def __eq__(self, other):
        val = True
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.matrix.get_item(i, j) != other.matrix.get_item(i, j):
                        val = False
            if val == True:
                print("Equal")
            else:
                print("Not equal")
        else:
            print("Can not compare")
        

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            add = [[self.matrix.get_item(i, j) + other.matrix.get_item(i, j) for i in range(self.cols)] for j in range(self.rows)]
            for i in add:
                print(*i)
            return add
        else:
            print("Can not add")

    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            sub = [[self.matrix.get_item(i, j) - other.matrix.get_item(i, j) for i in range(self.cols)] for j in range(self.rows)]
            for i in sub:
                print(*i)
            return sub
        else:
            print("Can not substract")

    def __mul__(self, other):
        if self.rows == other.cols and self.cols == other.rows:
            mul = [[0 for i in range(other.cols)] for j in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        mul[i][j] += self.matrix.get_item(i, k)*other.matrix.get_item(k, j)
            for i in mul:
                print(*i)
            return mul
        else:
            print("Can not multiply")




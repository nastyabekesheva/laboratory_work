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
                    if self.matrix.__getitem__(i, j) != other.matrix.__getitem__(i, j):
                        val = False
            if val == True:
                print("Equal")
            else:
                print("Not equal")
        else:
            print("Can not compare")

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            add = [[self.matrix.__getitem__(i, j) + other.matrix.__getitem__(i, j) for i in range(self.cols)] for j in range(self.rows)]
            for i in add:
                print(*i)
            return add
        else:
            print("Can not add")

    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            sub = [[self.matrix.__getitem__(i, j) - other.matrix.__getitem__(i, j) for i in range(self.cols)] for j in range(self.rows)]
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
                        mul[i][j] += self.matrix.__getitem__(i, k)*other.matrix.__getitem__(k, j)
            for i in mul:
                print(*i)
            return mul
        else:
            print("Can not multiply")

if __name__ == '__main__':
    n = int(input("Enter amount of rows: "))
    m = int(input("Enter amount of columns: "))
    u = AnyMatrix(n, m)
    print("\nCreating class object...\n")
    n1 = int(input("Enter amount of rows: "))
    m1 = int(input("Enter amount of columns: "))
    w = AnyMatrix(n1, m1)
    print("\nCreating class object...\n")
    uo = Overload(u)
    wo = Overload(w)
    print("\nOverloading addition: ")
    uo.__add__(wo).__print__()
    print("\nOverloading substraction: ")
    uo.__sub__(wo).__print__()
    print("\nOverloading multiplication: ")
    uo.__mul__(wo).__print__()
    print("\nOverloading comparison: ")


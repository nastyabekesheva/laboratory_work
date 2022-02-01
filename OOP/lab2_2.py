class AnyMatrix:
    def __init__(self, rows, cols):
        self.matrix = self.get_matrix(rows, cols)
        self.rows = rows
        self.cols = cols

    def get_matrix(self, rows, cols):
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(input())
        return matrix

    def check(self):
        negative = [[x for x in i if x < 0] for i in self.matrix]
        if len(negative) == 0:
            return True
        else:
            return False

    def get_size(self):
        print(f"The given matrix has {self.rows} rows and {self.cols} columns.\n Total size: {self.rows*self.cols}")

    def get_element(self, element):
        index = [(ind, row.index(element)) for ind, row in enumerate(self.matrix) if element in row]
        if len(index) == 0:
            print(f"Element {element} is not in the matrix")
        else:
            for i in range(len(index)):
                print(f"Element {element} is at row {index[i][0]}, column {index[i][1]}")
    
    def clear(self):
        del self.matrix[:]
        self.rows, self.cols = 0, 0
        print("Matrix has been cleared")

    def print(self):
        for i in self.matrix:
            print(*i)

class Matrix(AnyMatrix):
    def __init__(self, matrixs, rows, cols):
        super().__init__(rows, cols)
        if matrixs.check() == False:
            print("Negative integers detected. Plese refiil the matrix")
            self.matrixs = self.refill_matrix(rows, cols)
        else:
            self.matrixs = matrixs
            print("No negative integers detected")

    def refill_matrix(self, rows, cols):
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                x = int(input())
                if x < 0:
                    print("Plese enter a positive integer")
                    x = int(input())
                matrix[i][j] = x
        return matrix
            



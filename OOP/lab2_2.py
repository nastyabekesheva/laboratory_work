class AnyMatrix:
    def __init__(self, rows, cols):
        self.matrix = self.get_matrix(rows, cols)
        self.rows = rows
        self.cols = cols

    def __getmatrix__(self, rows, cols):
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(input())
        return matrix

    def __check__(self):
        negative = [[x for x in i if x < 0] for i in self.matrix]
        if len(negative) == 0:
            return True
        else:
            return False

    def __getsize__(self):
        print(f"The given matrix has {self.rows} rows and {self.cols} columns.\n Total size: {self.rows*self.cols}")

    def __getelement__(self, element):
        index = [(ind, row.index(element)) for ind, row in enumerate(self.matrix) if element in row]
        if len(index) == 0:
            print(f"Element {element} is not in the matrix")
        else:
            for i in range(len(index)):
                print(f"Element {element} is at row {index[i][0]}, column {index[i][1]}")
    
    def __clear__(self):
        del self.matrix[:]
        self.rows, self.cols = 0, 0
        print("Matrix has been cleared")

    def __print__(self):
        for i in self.matrix:
            print(*i)

    def __getitem__(self, item1, item2):
        return self.matrix[item1][item2]

    def __del__(self):
        print("Class object (matrix) deleted")


class Matrix(AnyMatrix):
    def __init__(self, matrix):
        if matrix.__check__() == False:
            print("Negative integers detected. Plese refiil the matrix")
            self.matrix = self.refill_matrix(matrix.rows, matrix.cols)
        else:
            self.matrix = matrix
            print("No negative integers detected")

    def __refill__(self, rows, cols):
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                x = int(input())
                if x < 0:
                    print("Plese enter a positive integer")
                    x = int(input())
                matrix[i][j] = x
        return matrix
            
if __name__ == '__main__':
    n = int(input("Enter amount of rows: "))
    m = int(input("Enter amount of columns: "))
    matrix = AnyMatrix(n, m)
    print("Creating class object...\n")
    print("Enter values: \n")
    matrix.__getsize__()
    print("Your matrix: \n")
    matrix.__print__()
    val = int(input("Enter value to get"))
    matrix.__getelement__(val)
    print("Checking for negative values")
    pmatrix = Matrix(matrix)
    print("Your matrix: \n")
    pmatrix.__print__()
    print("Clearing the matrix")
    pmatrix.__clear__()
    pmatrix.__print__()




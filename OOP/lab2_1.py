def check_input(user_input):
    if user_input >= 0:
        return user_input
    else:
        print("Plese enter a positive integer")
        user_input = check_input(int(input()))
        return user_input

class Matrix:
    def __init__(self, rows, columns):
        self.matrix = self.fill_matrix(rows, columns)
        self.rows = rows
        self.columns = columns

    def fill_matrix(self, rows, columns):
        matrix = [[0 for j in range(columns)] for i in range(rows)]
        for i in range(rows):
            try:
                for j in range(columns):
                    matrix[i][j] = int(input())
            except IndexError:
                print(f"Error at row {i}, column {j}")
        return matrix

    def print_matrix(self):
        for i in self.matrix:
            print(*i)

    def get_element(self, element):
        indecies = [(index, row.index(element)) for index, row in enumerate(self.matrix) if element in row] 
        if len(indecies) == 0:
            print(f"Element {element} is not in the matrix")
        else:
            for i in range(len(indecies)):
                print(f"Element {element} is at row {indecies[i][0]}, column {indecies[i][1]}")

    def get_size(self):
        print(f"Your matrix has {self.rows} rows and {self.columns} columns\nTotal length: {self.rows*self.columns}")

    def clear_matrix(self):
        del self.matrix[:]
        print("Matrix has been cleared")
'''
class IntMatrix(Matrix):
    def __init__(self, rows, columns):
        super().__init__(matrix, rows, columns)

    def check(self):
        negative = [[x for x in i] for i in self.matrix if x < 0]
        if len(negative) == 0:
            print("All integers in this matrix are positive")
        else: 
            print("Negative inegers found. Refilling matrix...")
            self.matrix.refill()

    def refill(self):
        matrix = [[0 for j in range(columns)] for i in range(rows)]
        for i in range(rows):
            try:
                for j in range(columns):
                    matrix[i][j] = int(input())
            except IndexError:
                print(f"Error at row {i}, column {j}")
        self.matrix = matrix '''

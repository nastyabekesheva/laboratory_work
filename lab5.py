class TemplateMatrix:
    def __init__(self, rows, cols):
        self.matrix = self.__get__(rows, cols)

    def __get__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        matrix = []
        for i in range(rows):
            temp = input().split()
            if len(temp) == rows:
                matrix.append(int(j) for j in temp)
            else:
                print(f"Incorect input at row {i}. Plese try again")
        return matrix
    
    def __copy__(self, matrix):
        return self.matrix

    def __getitem__(self, i, j):
        return self.matrix[i][j]

    def __setitem__(self, item, i, j):
        self.matrix[i][j] = item

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

    def __transpose__(self):
        return [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
                        
    def __len__(self):
        return sum(len(i) for i in self.matrix)

    def __getrow__(self, row):
        return self.matrix[row]

    def __getcol__(self, col):
        temp = []
        for i in range(self.rows):
            temp.append(self.matrix[i][col])
        return temp

    def __print__(self):
        for i in self.matrix:
            print(*i)

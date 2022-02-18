from lab2_2 import AnyMatrix

class OverloadData:

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


    def __rshift__(self, other):
        other.item = input()

    def __lshift__(self, other):
        print(other.item)
    

cout = OverloadData()
cin = OverloadData()

a = OverloadData()
cin >> a
cout << a


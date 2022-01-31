from lab2 import Complex

class Overload(Complex):
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        return Complex(self.real_part + other.real_part, self.im_part + other.im_part)

    def __sub__(self, other):
        return Complex(self.real_part - other.real_part, self.im_part - other.im_part)

    def __eq__(self, other):
        if self.im_part == other.im_part and self.real_part == self.real_part:
            print("Equal")
        else:
            print("Not equal")

    

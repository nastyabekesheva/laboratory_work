class Complex:
    def __init__(self, real_part, im_part):# creating a complex number
        self.real_part = real_part
        self.im_part = im_part

    def display(self):# printing a complex number as a+b*i where i = sqrt(-1)
        print(f"{self.real_part} + {self.im_part}i")

    def add(self, other):# adding two complex numbers
        return Complex(self.real_part + other.real_part, self.im_part + other.im_part)

    def substract(self, other):# substracting two complex numbers
        return Complex(self.real_part - other.real_part, self.im_part - other.im_part)

    def multiply(self, other):# multiplying two complex numbers
        return Complex(self.real_part * other.real_part - self.im_part * other.im_part, self.im_part * other.real_part + self.real_part * other.im_part)

    def divide(self, other):# dividing two complex numbers
        a, b, c, d = self.real_part, self.im_part, other.real_part, other.im_part
        return Complex(float((a*c + b*d)/(c**2+d**2)), float((b*c - a*d)/(c**2 + d**2)))

    def __del__(self):# a classic destructor
        print("Class object(Complex number) deleted.")

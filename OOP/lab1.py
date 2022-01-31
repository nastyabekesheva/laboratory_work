class Dog:
    info = "set info about your dog"
    def __init__(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

def main():
    name = input("Name: ")
    my_dog = Dog(name)
    my_dog.info
    age = input("Age: ")
    my_dog.set_age(age)
    weight = input("Weight: ")
    my_dog.set_weight(weight)
    print(f"Your dog's name is {my_dog.name}, it's age: {my_dog.age}, weight: {my_dog.weight}")

main()

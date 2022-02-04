class Dog:
    info = "set info about your dog"
    def __init__(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def get_info(self):
        print(f"Your dog's name is {self.name}, age {self.age}, weight {self.weight}")

print(Dog.info)

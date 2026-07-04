class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        def show(self):
            print(f"Name: {self.name}, Age: {self.age}")
        def speak(self):
            print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return "Meow"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return "Woof"
    def speak(self):
        return "Woof"
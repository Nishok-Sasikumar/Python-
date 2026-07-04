#Simple method 
class Student:

    def say_hello(self):
        print("Hello")

s1 = Student()

s1.say_hello()

#Instace method --> use self to access the instance attributes and methods
class Student:

    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

s1 = Student("John")

s1.show()

#Class method --> use @classmethod decorator to define a class method. It takes cls as the first parameter instead of self. Class methods can access and modify class-level attributes.
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
#Static method --> use @staticmethod decorator to define a static method. It does not take self or cls as the first parameter. Static methods are used for utility functions that do not require access to instance or class attributes.
class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(10,20))


class Mother:
    hair_color = "black"
    eye_color = "brown"
class Father:
    hair_color = "brown"
    eye_color = "blue"
class Child(Mother, Father):
    pass
c1 = Child()
print("Child's hair color:", c1.hair_color)
print("Child's eye color:", c1.eye_color)
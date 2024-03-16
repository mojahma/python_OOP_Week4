class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello : {self.name}, You are : {self.age} years old and your gender is: {self.gender}")
        
        
person1 = Person("John", 25, "Male")

person1.introduce()
    
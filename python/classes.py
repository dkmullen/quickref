class Person:
    def __init__(self, name, age): # self refers to the class itself
        self.name = name
        self.age = age

    def intro_me(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")
        print("Hello, I am", self.name, "and I am", self.age, "years old.")

p1 = Person("Dennis", "54")
p1.intro_me()

p1.age = 55
p1.intro_me()

del p1.age
del p1

class MyClass:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def __add__(self, other):
        return MyClass(self.name + other.name, self.age + other.age)

    def printname(self):
        print("My name is %s" % self.name)

    def printage(self):
        print("My age is %d" % self.age)


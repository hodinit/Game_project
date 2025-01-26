class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    def myfunc(self):
        print("hello "+ self.name)

p1 = Person('john', 44)
p1.myfunc()

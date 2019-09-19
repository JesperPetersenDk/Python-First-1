class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def mamefunc(self):
        print(self.name, self.age)


class Student(Person):
    pass


p1 = Person("Jesper", 26)
p1.mamefunc()

x = Student("mike", 50)
x.mamefunc()




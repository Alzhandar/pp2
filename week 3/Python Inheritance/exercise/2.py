class Person:
    def __init__(self,fname) -> None:
        self.firstname=fname
    def printname(self):
        print(self.firstname)
class Student(Person):
    pass
x=Student("Mike")
x.printname()
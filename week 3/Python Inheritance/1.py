class Person:
    def __init__(self,fname,lname) -> None:
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("John","Doe")
x.printname()
class Student(Person):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)
        self.graduationyear=2019
x=Student("Mike","Olsen")
x.printname()
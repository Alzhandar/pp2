class Person:
    def __init__(self,fname,lname) -> None:
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("John","Doe")
x.printname()
class Student(Person):
    def __init__(self, fname, lname,year) -> None:
        super().__init__(fname, lname)
        self.graduationyear=year
x=Student("Mike","Olsen",2019)
x.printname()
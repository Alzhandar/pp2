class Human:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __str__(self) -> str:
        return self.name+' '+self.age
p1=Human("John","36")
p1.age="40"
print(p1)
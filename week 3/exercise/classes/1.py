class IOstring():
    def __init__(self,s):
        self.s=s
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
xx = IOstring()
xx.getString()
xx.printString()
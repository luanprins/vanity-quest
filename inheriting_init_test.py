class MainClass():
    def __init__(self):
        self.nothing = 2000

class SubClass(MainClass):
    pass

tester = SubClass()

print(tester.nothing)
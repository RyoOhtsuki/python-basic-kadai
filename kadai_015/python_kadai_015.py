class Human:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name, self.age)

human1 = Human("Ryo", 34)
human1.printinfo()

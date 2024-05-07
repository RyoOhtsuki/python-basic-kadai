class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def check_adult(self):
        if self.age >= 20:
            print("You are an adult")
        else:
            print("You are not an adult")

humans = [Human("Nick", 10), Human("James", 20), Human("Sara", 30)]

for human in humans:
    print(human.name, human.age)
    human.check_adult()




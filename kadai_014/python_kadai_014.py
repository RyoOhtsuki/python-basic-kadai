class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

user1 = User("Ryo", 34, "male")
print(user1.name, user1.age, user1.gender)


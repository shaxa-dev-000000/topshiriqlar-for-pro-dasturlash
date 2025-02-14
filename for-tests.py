class Person:
    level = "junior"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        print(self.name)

    def get_level(self, lvl):
        self.level = lvl


person = Person("shaxriyor", 18, "man")
person.get_level(lvl="middle")

print(person.level)

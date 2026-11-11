class Person :
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("My name is above")

john = Person("John Smith")
print(john.name)
john.talk()
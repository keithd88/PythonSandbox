class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def sayHi(self):
        print(f"Hi! My name is {self.getName()}.")

    def sayBye(self):
        print(f"Bye!")
    
bob = Person("Bob")
bob.sayHi()
bob.sayBye()
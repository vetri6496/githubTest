""" OBJCET ORIENTED PROGRAMMING"""

""" CLASS """

class Person:

    def __init__(self, name):
        print(f"{name}, is created here")
    def eat(self, name):
        print(f"{name} I can eat")
    
    def talk(self):
        print("I can talk")


def main():

    p1 = Person("John")
    p2 = Person("cena")

    p1.eat("John")
    p1.talk()
    p2.eat("Cena")
    p2.talk()

main()
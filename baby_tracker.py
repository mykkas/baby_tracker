# A program to track your infant's feeding/sleeping schedule

class Baby:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight  = weight
        self.height = height


def intro():
    print("Welcome and congratulations on your bundle of joy!\n")
    print("This application is designed to help you keep track of your baby's first few months.\n\n")
    print("Let's start by gettting some basic info!")
    name = input("Baby's name: ")
    weight = input("Baby's weight in grams: ")
    height = input("Baby's height in cm: ")
    return name, weight, height


name, weight, height = intro()

baby_1 = Baby(name, weight, height)

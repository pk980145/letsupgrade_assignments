class Animal:
    def make_sound(self):
        print("general animal's sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

obj = Animal()
obj1 = Dog()
obj2 = Cat()

def animal_sound_in_zoo():
    option = input("Enter the name of Animal")
    if option.lower() == "dog":
        obj1.make_sound()
    elif option.lower()== "cat":
        obj2.make_sound()
    else:
        obj.make_sound()

animal_sound_in_zoo()
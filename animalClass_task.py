class Animal:
    def voice(self):
        pass

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        
    def voice(self):
        print("мяу-мяу")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

    def voice(self):
        print("гав-гав")


class Cow(Animal):
    def __init__(self):
        Animal.__init__(self)

    def voice(self):
        print("мууууу")

animalCat = Cat()
animalCat.voice()

animalDog = Dog()
animalDog.voice()

animalCow = Cow()
animalCow.voice()

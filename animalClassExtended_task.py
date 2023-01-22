def printAnimalNum():
        print(Animal.animal_num, "было создано экземпляров")

class Animal:
    animal_num = 0
    printAnimalNum = staticmethod(printAnimalNum)

    def __init__(self):
        Animal.animal_num+=1
        
    def voice(self):
        pass

class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        
    def voice(self):
        print("мяу-мяу")


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()

    def voice(self):
        print("гав-гав")


class Cow(Animal):
    def __init__(self):
        super(Cow, self).__init__()

    def voice(self):
        print("мууууу")

cat1 = Cat()
dog1 = Dog()
cow1 = Cow()

printAnimalNum()
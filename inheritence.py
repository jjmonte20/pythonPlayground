class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')
    #   pass is used when there is no need to add additional conditions for a class


class Cat(Mammal):
    pass
    #  same as before


dog1 = Dog()
dog1.walk()
dog1.bark()
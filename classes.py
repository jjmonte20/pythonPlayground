# Classes can be used to define complex things
class Point:
    # init method makes a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point(10, 20)
point.x = 11
# can change object values after the fact
print(point.x)
# this creates the object of the class point

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello my name is {self.name}!')

julian = Person("Julian")
julian.talk()
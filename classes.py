# Classes can be used to define complex things
class Point:
    def move(self):
        print('move')


    def draw(self):
        print('draw')


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
# this creates the object of the class point
point1.draw()
# prints draw from point 1


point2 = Point()


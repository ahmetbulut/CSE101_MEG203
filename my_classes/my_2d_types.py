import math

class Point:
    """
    Represents a point in 2D space.
    Each point has an x and a y dimension, i.e. value.
    Each point has those two attributes.
    """

    # constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #human readable string representation of the object, i.e., print
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)


    def distance(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y

        return math.sqrt(delta_x**2 + delta_y**2)


p = Point(2, 3) # instantiating an object = creating an object

print(type(p))
print("X dimension: %d; Y dimension: %d" % (p.x, p.y))

# instances of Point class.
p1 = Point(3,4)
origin = Point(0,0)

yet_another_reference = origin

print("The distance is", p1.distance(origin))
print("The distance between", p1, "and", origin, "is:", yet_another_reference.distance(p1))

origin.x = 100 #mutable, this is possible


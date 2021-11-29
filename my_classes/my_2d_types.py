import math
from builtins import list


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

    #an example of operator overloading.
    def __add__(self, other):
        #self is a point, i.e., a vector
        #other is a point, i.e., a vector
        #I want to add those two vectors, and return the result vector.
        #this operation is a vector addition.
        return Point(self.x + other.x, self.y + other.y)

    #implemantation of the Pythagorean theorem
    def distance(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        return math.sqrt(delta_x**2 + delta_y**2)

    def distance_from_origin(self):
        origin = Point(0,0)
        return self.distance(origin)

class Rectangle:
    """
    Represents a rectangle in 2D space.

    (Xtl, Ytl)-----------(Xtr,Ytr)
              |         |
              |         |
              |         |
    (Xbl,Ybl) ----------- (Xbr,Ybr)
    Each rectangle is going to be specified via bottom-left corner,
    and its width and height information.
    """

    def __init__(self, bottom_left, width, height):
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

    def __str__(self):
        return "Bottom left corner %s, width=%d, height=%d" % (
            self.bottom_left, self.width, self.height)

    # compute the area of the rectangle
    def area(self):
        return self.height * self.width

    def distance_from_origin(self):
        """
        origin is a point with x = 0, y = 0; origin = Point(0,0)
        rectangle's bottom left corner is also a point; self.bottom_left; other = Point(x,y)
        distance from origin can be computed as origin.distance(other)
        :return: distance from origin
        """
        return self.bottom_left.distance_from_origin()

def polymorphic_function(list_of_objects):
    for item in list_of_objects:
        print(item.distance_from_origin())

def compute_the_area_if_it_makes_sense(list_of_objects):
    for item in list_of_objects:
        #type-based check, dispatching
        if isinstance(item, Rectangle):
            print(item.area())
        else:
            print("ERROR: Not able to compute the area!")

p = Point(2,3) # instantiating an object = creating an object
print(type(p))
print("X dimension: %d; Y dimension: %d" % (p.x, p.y))

# instances of Point class.
p1 = Point(3,4)
origin = Point(0,0)

yet_another_reference = origin

print("The distance is", p1.distance(origin))
print("The distance between", p1, "and", origin, "is:", yet_another_reference.distance(p1))

origin.x = 100 #mutable, this is possible

r = Rectangle(p1,10,10)
print("The distance from the origin to the rectangle [with spec: %s] is %.2f" %
      (r, r.distance_from_origin()))

l = [p, p1, origin, r]
polymorphic_function(l)

#print(isinstance(r, Point))
#print(isinstance(r, Rectangle))

compute_the_area_if_it_makes_sense(l)

print(p + p1)

class Point:
    """
    Represents a point in 2D space.
    Each point has an x and a y dimension, i.e. value.
    Each point has those two attributes.
    """

    # constructor method
    def __init__(self, x , y):
        self.x = x
        self.y = y


p = Point(2, 3) # instantiating an object = creating an object

print(type(p))
print("the value on the X dimension is %d; the value on the Y dimension is %d" % (p.x, p.y))

# instances of Point class.
p1 = Point(14,78)
origin = Point(0,0)

print("Origin is represented as (%d, %d)" % (origin.x, origin.y))

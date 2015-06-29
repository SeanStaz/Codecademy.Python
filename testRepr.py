    #Define a Point3D class that inherits from object
    #Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x, self.y, self.z
    #Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the following format: (x, y, z).
    #Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3.
    #Finally, print my_point.

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)

print my_point

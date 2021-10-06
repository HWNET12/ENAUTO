class Circle():
    radius = 0;
    
    def calcCircumference(self):
        return 3.141 * 2 * self.radius
    
# We invoke it by creating an instance of the class
# This creates a new instance of Circle class

circleA = Circle()
circleA.radius = 15

print(circleA.calcCircumference())

circleB = Circle()
circleB.radius = 11

print(circleB.calcCircumference())
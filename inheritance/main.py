# Inheritance allows one class to reuse the attributes and methods of another class.

# For example, a square is a special type of rectangle.

# A square has:
# - A width.
# - A height.
# - Equal width and height.
# Therefore, instead of writing everything again, we can make Square inherit from Rectangle.


class Rectangle:

    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height =  height

rect = Rectangle(10, 90)

print(rect.width)
print(rect.height)

rect.set_width(20)
rect.set_height(30) 

print(rect.width)
print(rect.height)


#inheritace syntax
class square(Rectangle): #this means that square is the child class and Rectangle is the parent class
    pass

sq = square(10, 10)
print(sq.width)
print(sq.height)
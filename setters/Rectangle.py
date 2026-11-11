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

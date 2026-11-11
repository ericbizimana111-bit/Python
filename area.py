class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def get_area(self):
        
        return self.width * self.height

rect = Rectangle(10, 5)

print(rect.get_area())


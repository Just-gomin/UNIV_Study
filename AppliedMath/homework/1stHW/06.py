class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        a = self.width * self.height
        print("This rectangle's Area\n{0}".format(a))

    def diagonal(self):
        di = (self.width**2 + self.height**2)**(1/2)
        print("This rectangle's Diagonal\n{0}".format(di))


rect1 = Rectangle(4, 5)
rect1.area()
rect1.diagonal()

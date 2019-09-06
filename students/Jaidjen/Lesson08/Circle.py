import math

class Circle():

    def __init__(self, r):
        self.radius = r
        self.c = Circle

    def the_radius(self):
        c = Circle(4)
        print(c.radius)

    def diameter(self):
        c=Circle(4)
        while True:
            try:
                diameter = input("Please enter the diameter of the circle:  ")
            except ValueError:
                print("Please enter a number!")
            else:
                print("The diameter of the circle is: " + (str(diameter)))
                break


    def area(self):
        area = self.radius ** 2 * 3.14
        print("The area of the circle is:" + (str(area)))


    def userdiameter(cls):
        c = Circle.diameter(8)
        Circle.userdiameter=classmethod(Circle.userdiameter)

    def __str__(self):
        c = Circle(4)
        return 'Circle with rsdius: {self.radius}'.format(self=self)


    def __repr__(self):
        c = Circle(4)
        repr(self.radius)

    def __add__(self, other):
        c1 = Circle(2)
        c2 = Circle(4)
        return(c1, c2)


    def __mul__(self, other):
        return Circle(c2*3)


    def __gt__(self, other):
        return other>self

    def __lt__(self, other):
        return self<other

    def __eq__(self, other):
        return self == other
        c3 = Circle(4)
        return c2 == c3

    def circle_sort(self):
        c = ['Circle(6)', 'Circle(7)', 'Circle(8)', 'Circle(4)', 'Circle(0)', 'Circle(2)', 'Circle(3)', 'Circle(5)', 'Circle(9)', 'Circle(1)']
        print(c)
        c.sort()
        print(c)



NewCircle = Circle(8)
print(NewCircle.diameter())
print(NewCircle.area())
print(NewCircle.userdiameter())
print(NewCircle.__str__())
print(NewCircle.__repr__())
print(NewCircle.__add__(2))
print(NewCircle.__mul__(2))
print(NewCircle.__lt__(2))
print(NewCircle.__gt__(2))
print(NewCircle.__eq__(2))
print(NewCircle.circle_sort())

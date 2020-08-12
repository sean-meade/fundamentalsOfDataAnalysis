import numpy as np

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

print(x)
print(type(x))

class Point:
    x = 0
    y = 0

p1 = Point()

print(p1.x)

p1.x = 3

p2 = Point()

print(p2.x)
print(p1.x)

class Point2():
    x = 0
    y = 0

    def mag(self):
        return self.x*self.x + self.y*self.y

p1 = Point2()
p2 = Point2()

p1.x = 5
p1.y = 15
p2.y = 10

print(p1.mag())
print(p2.mag())


x1 = [1, 2, 3, 4, 5]
x = np.array([1, 2, 3, 4, 5])

print(x.sum())
print(x1.sum())

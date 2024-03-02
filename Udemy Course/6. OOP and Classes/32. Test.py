# Реализуйте методы класса Line, который принимает на вход координаты в виде двух кортежей, а возвращает угол наклона и длину этой линии.
# distance = sqrt((x2 — x1)^2 + (y2 — y1)^2)  d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
# slope = (y2 — y1) / (x2 — x1)
class Line():
    def __init__(self, coor1, coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    def coordinates (self):
        return f"X1 = {self.x1}, X2 = {self.x2}, Y1 = {self.y1}, Y2 = {self.y2}"
    def distance(self):
        import math
        return (math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)))
    def slope(self):
        return ((self.y2 - self.y1)/(self.x2 - self.x1))

coordinate1 = (3, 2)
coordinate2 = (8, 10)
line = Line (coordinate1, coordinate2)
print (line.coordinates())
print (line.distance())
print (line.slope())

# Реализуйте методы класса Cylinder, который принимает на вход координаты в виде кортежа, а возвращает объем и площадь поверхностии.
# volume = π·R²·h
# surface = 2πR² + 2πRH
class Cylinder():
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
    def parameters (self):
        return f"Height = {self.height}, Radius = {self.radius}"
    def volume(self):
        import math
        return (math.pi * self.radius**2 * self.height)
    def surface(self):
        import math
        return (2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height)
cylinder = Cylinder(2,3)
print (cylinder.parameters())
print ('Объем: ',cylinder.volume())
print ('Площадь: ',cylinder.surface())
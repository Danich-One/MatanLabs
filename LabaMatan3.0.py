import numpy as np
from shapely.geometry import Point, Polygon


def f(x, y):
    return x**2 + x*y + y**2

def inside(x, y, points):
    point = Point(x, y)
    polygon = Polygon(points)
    return polygon.contains(point)

def intersects(x, y, points, h):
    polygon = Polygon(points)
    square = Polygon(((x+h/2, y-h/2), (x+h/2, y+h/2), (x-h/2, y-h/2), (x-h/2, y+h/2)))
    return polygon.intersects(square)


print('введите количество вершин многоугольника в области [−18, 17]×[−64, 71]:') # noqa
num = input()
num = int(num)

bound = np.array([[-18, 17], [-64, 71]]) # noqa
points = np.zeros((num, 2))
I, h = 0, 1
R = 85 * h**2 / 6

for i in range(num):
    print('введите координаты', i+1 ,'точки (x, y) через пробел:') # noqa
    points[i, 0], points[i, 1] = input().split()
    while points[i, 0] < bound[0, 0] or points[i, 0] > bound[0, 1] or points[i, 1] < bound[1, 0] or points[i, 1] > bound[1, 1]:
        print('вершина не в области G, введите заново:') # noqa
        points[i, 0], points[i, 1] = map(float, input().split())

X = np.arange(bound[0, 0]+h/2, bound[0, 1]+h/2, h)
Y = np.arange(bound[1, 0]+h/2, bound[1, 1]+h/2, h)

for x in X:
    for y in Y:
        if inside(x, y, points):
            I += f(x, y) * 2 * h**2
        elif intersects(x, y, points, h):
            R += f(x, y) * h**2

print('Интеграл = ', I)
print('Погрешность = ', R)
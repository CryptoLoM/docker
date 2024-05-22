from math import pi

def circle_area(radius):
    if radius<0:
        raise ValueError('Impossible value')
    if type(radius) not in [int, float]:
        raise TypeError('Impossible types')
    return pi*radius**2
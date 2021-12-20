# A component responsible solely for the wholesale creation of objects.
from cmath import cos, sin


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # PointFactory is a inner class here
    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

        def __str__(self):
            return f"x:{self.x}, y:{self.y}"


if __name__ == '__main__':
    p = Point(2, 3)
    pe = Point.PointFactory.new_polar_point(5, 7)
    ab = Point.PointFactory.new_cartesian_point(4, 6)
    print(pe)
    print(ab)

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Open closed Principle - Open for extension and closed for modification.
# Once the class is deployed no modification is allowed according to OCP, it could be available for extension though
class ProductFilter:
    @staticmethod
    def filter_by_color(products1, color):
        for p1 in products1:
            if p1.color == color:
                yield p1

    @staticmethod
    def filter_by_size(products1, size):
        for p1 in products1:
            if p.size == size:
                yield p1

    @staticmethod
    def filter_by_size_and(products1, size, color):
        for p1 in products1:
            if p1.color == color and p1.size == size:
                yield p1


# OCP-Approach
# Specification - Base class.
class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    products = [apple, tree, house]
    pf = ProductFilter()
    print("Green products (Old approach/Violation OCP)")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f"{p.name} is Green")

    print("OCP Approach")
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f"{p.name} is Green")

    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f"{p.name} is Large")

    print("OCP Approach - AND ")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f"{p.name} is large and blue")

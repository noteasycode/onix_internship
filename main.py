import math


class Shape():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    @classmethod
    def get_distance(cls, figure_1, figure_2):
        pass


class Circle(Shape):
    def __init__(self, pos_x, pos_y, radius):
        super().__init__(pos_x, pos_y)
        self.radius = radius

    def get_center(self):
        return self.pos_x, self.pos_y

    def get_area(self):
        return math.pi * self.radius ** 2

    def move(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y
        return self.pos_x, self.pos_y


class Square(Shape):
    def __init__(self, pos_x, pos_y, side):
        super().__init__(pos_x, pos_y)
        self.side = side

    def get_center(self):
        return self.pos_x, self.pos_y

    def get_vertex(self):
        pass

    def get_area(self):
        return self.side ** 2

    def move(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y
        return self.pos_x, self.pos_y


class Triangle(Shape):
    def __init__(self, pos_x, pos_y, side):
        super().__init__(pos_x, pos_y)
        self.side = side

    def get_center(self):
        return self.pos_x, self.pos_y

    def get_vertex(self):
        pass

    def get_area(self):
        return

    def move(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y
        return self.pos_x, self.pos_y


if __name__ == '__main__':
    result = Circle(0, 0, 3)
    print(result.get_area())
    print(result.get_center())
    print(result.move(1, 1))
    print(result.get_center())

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Position) and \
               self.x == other.x and \
               self.y == other.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    __repr__ = __str__

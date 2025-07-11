class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
p1 = point(2,3)
p2 = point(5,6)
p3 = point(7,8)
p4 = point(9,10)
print(p1)
print(p2)
print(p3)
print(p4)
class Vector(x,y):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Test_Vector():
    def test_create(self):
        v=Vector(x=1, y=2)
        assert(True)


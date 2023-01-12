#Task_3
class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        parallelogram_area = self.width * self.length
        return parallelogram_area

# p = Parallelogram(8, 15)
# print(f'Parallelogram area is {p.get_area()}')

class Square(Parallelogram):
    def __init__(self, width, length):
        Parallelogram.__init__(self, width, length)


    def get_area(self):
        square_area = 0
        if self.width == self.length:
            square_area = self.width * self.length
        else:
            print(f'Square area = {square_area} because values <width> and <length> are not equal')
        return square_area

s = Square(9, 9)
print(s.get_area())
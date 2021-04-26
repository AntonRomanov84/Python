class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def coat_area(self):
        return self.width / 6.5 + 0.5
    def jacket_area(self):
        return self.height * 2 + 0.3

    @property
    def total_area(self):
        return str(f'Общая площадь ткани: \n'
                   f' {(self.coat_area()) + (self.jacket_area())}')

class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.c_area = round(self.coat_area())
    def __str__(self):
        return f'Площадь ткани для пальто: {self.c_area}'

class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.j_area = round(self.jacket_area())
    def __str__(self):
        return f'Площадь ткани на костюм: {self.j_area}'

coat = Coat(10, 16)
jacket = Jacket(9, 11)
print(coat)
print(jacket)
print(coat.total_area)
print(jacket.total_area)
table_length = 10
table_width = 5


class TableMaterial(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_material(self):
        print(self.name)


class Wood(TableMaterial):
    SYMBOL = "W"

    def __init__(self, name, color):
        super(Wood, self).__init__(name, color)


class Metal(TableMaterial):
    SYMBOL = "M"

    def __init__(self, name, color):
        super(Metal, self).__init__(name, color)


class Glass(TableMaterial):
    SYMBOL = "G"

    def __init__(self, name, color):
        super(Glass, self).__init__(name, color)


class Aluminum(TableMaterial):
    SYMBOL = "A"

    def __init__(self, name, color):
        super(Aluminum, self).__init__(name, color)


border = Wood("wood", "black")
inside1 = Metal("steal", "silver")
inside2 = Glass("glass", "none")

print(border.SYMBOL * table_length)
print(border.SYMBOL + inside1.SYMBOL * (table_length - 2) + border.SYMBOL)

for i in range(2, table_width - 2):
    print(border.SYMBOL + inside2.SYMBOL * (table_length - 2) + border.SYMBOL)

print(border.SYMBOL + inside1.SYMBOL * (table_length - 2) + border.SYMBOL)
print(border.SYMBOL * table_length)

class Table:
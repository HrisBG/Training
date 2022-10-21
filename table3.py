class TableMaterial(object):
    SYMBOL = "-"
    PRICE = None

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_material(self):
        print(self.name)


class Wood(TableMaterial):
    SYMBOL = "W"
    PRICE = 8

    def __init__(self, name, color):
        super(Wood, self).__init__(name, color)


class Metal(TableMaterial):
    SYMBOL = "M"
    PRICE = 5

    def __init__(self, name, color):
        super(Metal, self).__init__(name, color)


class Glass(TableMaterial):
    SYMBOL = "G"
    PRICE = 6

    def __init__(self, name, color):
        super(Glass, self).__init__(name, color)


class Aluminum(TableMaterial):
    SYMBOL = "A"
    PRICE = 10

    def __init__(self, name, color):
        super(Aluminum, self).__init__(name, color)


class Empty(TableMaterial):
    SYMBOL = "E"
    PRICE = 0

    def __init__(self, name, color):
        super(Empty, self).__init__(name, color)


class Table(object):

    def __init__(self, plate):
        self.plate = plate

    def table_price(self):
        price = 0
        for row in self.plate:
            for col in row:
                price += col.PRICE
        return price


class Printer(object):
    def __init__(self, table):
        self.table = table

    def print_table(self):
        result = ""
        for i in self.table.plate:
            i = [z.SYMBOL for z in i]
            result += '\t'.join(map(str, i)) + '\n'
        print(result)


user_plate = [
    [Wood, Metal, Wood],
    [Wood, Glass, Wood],
    [Glass, Empty, Glass],
    [Aluminum, Empty, Aluminum]
    ]

x = Table(user_plate)
pp = Printer(x)
pp.print_table()

print(x.table_price())

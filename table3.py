class TableMaterial(object):
    SYMBOL = "-"

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def print_material(self):
        print(self.name)


class Wood(TableMaterial):
    SYMBOL = "W"

    def __init__(self, name, color, price):
        super(Wood, self).__init__(name, color, price)


class Metal(TableMaterial):
    SYMBOL = "M"

    def __init__(self, name, color, price):
        super(Metal, self).__init__(name, color, price)


class Glass(TableMaterial):
    SYMBOL = "G"

    def __init__(self, name, color, price):
        super(Glass, self).__init__(name, color, price)


class Aluminum(TableMaterial):
    SYMBOL = "A"

    def __init__(self, name, color, price):
        super(Aluminum, self).__init__(name, color, price)


class Table(object):

    def __init__(self, plate):
        self.plate = plate

    def table_price(self):
        price = 0
        dd = {
            "W": 8,
            "G": 6,
            "M": 5,
            "A": 10
        }
        for i in self.plate:
            for j in i:
                if j in dd:
                    y = dd.get(j)
                    price += y
        return price


class Printer(object):
    def __init__(self, table):
        self.table = table

    def print_table(self):
        result = ""
        for i in self.table.plate:
            result += '\t'.join(map(str, i)) + '\n'
        print (result)


user_plate = [
    ["W", "M", "W"],
    ["W", "G", "W"],
    ["G", None, "G"],
    ["A", None, "A"]
    ]

x = Table(user_plate)
pp = Printer(x)
pp.print_table()

metal = Metal("Steal", "silver", 5)
glass = Glass("Glass", "White", 6)
wood = Wood("Wood", "Black", 8)
alum = Aluminum("Aluminum", "while", 10)


print(x.table_price())

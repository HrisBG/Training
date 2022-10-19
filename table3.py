# table_length = 10
# table_width = 5


class TableMaterial(object):
    SYMBOL = "-"

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

# print(border.SYMBOL * table_length)
# print(border.SYMBOL + inside1.SYMBOL * (table_length - 2) + border.SYMBOL)
#
# for i in range(2, table_width - 2):
#     print(border.SYMBOL + inside2.SYMBOL * (table_length - 2) + border.SYMBOL)
#
# print(border.SYMBOL + inside1.SYMBOL * (table_length - 2) + border.SYMBOL)
# print(border.SYMBOL * table_length)


class Table(object):

    def __init__(self, table_length, table_width, material):
        self.table_length = table_length
        self.table_width = table_width
        self.material = material
        self.plate = []

        for i in range(self.table_width):
            self.plate.append([])
            for j in range(self.table_length):
                self.plate[i].append(self.material)

    # def TableConfigurator(self, length, width, material):
    #     pass


class Printer(object):
    def __init__(self, table):
        self.table = table

    def print_table(self):
        result = ""
        for i in self.table.plate:
            result += '\t'.join(map(str, i)) + '\n'
        print (result)


room_table = Table(5, 3, Wood.SYMBOL)


pp = Printer(room_table)
pp.print_table()

# room_table.TableConfigurator(1, 1, Metal.SYMBOL)
# pp = Printer(room_table)
# pp.print_table()


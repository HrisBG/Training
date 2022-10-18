#table_length = int(input("Please insert table length: "))
#table_width = int(input("Please insert table width: "))
table_length = 10
table_width = 5


class TableMaterial:

    def __init__(self, material, color, symbol):
        self.material = material
        self.color = color
        self.symbol = symbol

    def print_material(self):
        print(self.material)


class Wood(TableMaterial):
    def __init__(self, material, color, symbol):
        super().__init__(material, color, symbol)


class Metal(TableMaterial):
    def __init__(self, material, color, symbol):
        super().__init__(material, color, symbol)


class Glass(TableMaterial):
    def __init__(self, material, color, symbol):
        super().__init__(material, color, symbol)


border = Wood("wood", "black", "W")
inside1 = Metal("steal", "silver", "S")
inside2 = Glass("glass", "none", "G")


print(border.symbol * table_length)
print(border.symbol + inside1.symbol * (table_length - 2) + border.symbol)

for i in range(2, table_width - 2):
    print(border.symbol + inside2.symbol * (table_length - 2) + border.symbol)

print(border.symbol + inside1.symbol * (table_length - 2) + border.symbol)
print(border.symbol * table_length)


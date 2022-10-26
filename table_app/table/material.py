class TableMaterial(object):
    SYMBOL = "-"
    PRICE = None

    def __init__(self, color=""):
        self.color = color


class Wood(TableMaterial):
    SYMBOL = "W"
    PRICE = 10


class Metal(TableMaterial):
    SYMBOL = "M"
    PRICE = 5


class Glass(TableMaterial):
    SYMBOL = "G"
    PRICE = 6


class Aluminum(TableMaterial):
    SYMBOL = "A"
    PRICE = 10


class Empty(TableMaterial):
    SYMBOL = " "
    PRICE = 0

class TableMaterial(object):
    SYMBOL = "-"
    PRICE = None
    NAME = None
    STRENGTH = None
    COLOR = None


class Wood(TableMaterial):
    SYMBOL = "W"
    PRICE = 10
    NAME = 'PINE'
    STRENGTH = 21
    COLOR = 'BROWN'


class Metal(TableMaterial):
    SYMBOL = "M"
    PRICE = 6
    NAME = 'MET'
    STRENGTH = 18
    COLOR = 'METALIC'


class Glass(TableMaterial):
    SYMBOL = "G"
    PRICE = 8
    NAME = 'COLOR GLASS'
    STRENGTH = 5
    COLOR = 'YELLOW'


class Aluminum(TableMaterial):
    SYMBOL = "A"
    PRICE = 10
    NAME = 'Alum'
    STRENGTH = 16
    COLOR = "WHITE"


class Empty(TableMaterial):
    SYMBOL = " "
    PRICE = 0
    NAME = ' '
    STRENGTH = ' '
    COLOR = ' '

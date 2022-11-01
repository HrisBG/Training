from table_app.table.table_material import *
from table_app.table.table_logic import *
from table_app.table.table_printer import *
from table_app.table.custom_error import *

user_plate = [
    [Wood, Metal, Wood],
    [Wood, Glass, Wood],
    [Glass, Empty, Glass],
    [Aluminum, Empty, Aluminum]
    ]

try:
    x = TableLogic(user_plate)
    #x = TableLogic.logic(user_plate)
    #x = TableLogic.from_list(user_plate)
    print(x)
    print('-' * 10)
    #x.price = 99
    print(x.price)
    pp = TablePrinter(x.template)
    param = input('Please insert option:')
    pp.print(param)


except TableConfigError:
    print("Please check table configuration")

except TablePriceError:
    print("Check Material prices")

except PrinterConfigError:
    print("Check printer input data")

except Exception as e:
    print(e)

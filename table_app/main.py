from table_app.table.material import *
from table_app.table.table_logic import *
from table_app.table.printer import *
from table_app.table.custom_error import *

user_plate = [
    [Wood, Metal, Wood],
    [Wood, Glass, Wood],
    [Glass, Empty, Glass],
    [Aluminum, Empty, Aluminum]
    ]

try:
    x = Table(user_plate)
    print(x.app_plate)
    x.table_price()
    print(x.table_price())
    pp = Printer(x.app_plate)
    pp.print_table("PRICE")
    pp.print_table("SYMBOL")

except TableConfigError:
    print("Please check table configuration")

except TablePriceError:
    print("Check Material prices")

except PrinterConfigError:
    print("Check printer input data")

except Exception as e:
    print(e)

from table_app.table.material import *
from table_app.table.table_logic import *
from table_app.table.printer import *

user_plate = [
    [Wood, Metal, Wood],
    [Wood, Glass, Wood],
    [Glass, Empty, Glass],
    [Aluminum, Empty, Aluminum]
    ]

x = Table(user_plate)
print(x.plate)
print(x.app_plate)
print(x.table_price())
pp = Printer(x.app_plate)
pp.print_table("PRICE")
pp.print_table("SYMBOL")




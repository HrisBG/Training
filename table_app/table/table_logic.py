from table_app.table.custom_error import *


class Table(object):

    def __init__(self, app_plate):
        self.app_plate = app_plate

        try:
            for row in self.app_plate:
                for col in row:
                    new = col()
                    place = row.index(col)
                    row.pop(place)
                    row.insert(place, new)
        except Exception as e:
            raise TableConfigError(e)

    # calculate table price

    def table_price(self):
        try:
            price = 0
            for row in self.app_plate:
                for col in row:
                    price += col.PRICE
            return price
        except Exception as e:
            raise TablePriceError(e)


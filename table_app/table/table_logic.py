class Table(object):

    def __init__(self, app_plate):
        self.app_plate = app_plate

        for row in self.app_plate:
            for col in row:
                new = col()
                place = row.index(col)
                row.pop(place)
                row.insert(place, new)

    # calculate table price
    def table_price(self):
        price = 0
        for row in self.app_plate:
            for col in row:
                price += col.PRICE
        return price

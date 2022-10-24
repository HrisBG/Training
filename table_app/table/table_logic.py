class Table(object):

    def __init__(self, plate):
        self.plate = plate
        self.app_plate = []
        self.row = len(self.plate)
        self.col = len(self.plate[0])

        for row in range(self.row):
            self.app_plate.append([])
            for col in range(self.col):
                i = self.plate[row][col]()
                self.app_plate[row].append(i)

    # calculate table price
    def table_price(self):
        price = 0
        for row in self.app_plate:
            for col in row:
                price += col.PRICE
        return price

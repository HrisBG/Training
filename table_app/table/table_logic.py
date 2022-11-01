from table_app.table.custom_error import *


class TableLogic(object):

    def __init__(self, template, table_price=0):
        self.template = template
        self.__price = table_price  # min value for table

    @staticmethod
    def logic(template):
        try:
            for row in template:
                for col in row:
                    new = col()
                    place = row.index(col)
                    row.pop(place)
                    row.insert(place, new)
            return TableLogic(template)
        except Exception as e:
            raise TableConfigError(e)

    @classmethod
    def from_list(cls, template):
        """ make object from 'list' """
        try:
            list_table = TableLogic.logic(template)
            return list_table
        except Exception as e:
            raise TableConfigError(e)

    @property
    def price(self):
        """ Calculate table price """
        #self.__price = 0
        try:
            for row in self.template:
                for col in row:
                    self.__price += col.PRICE
            return self.__price
        except Exception as e:
            raise TablePriceError(e)

    # @price.setter
    # def price(self, value):
    #     try:
    #         if value < self.__price:
    #             print("You need more money")
    #         else:
    #             self.__price = value
    #     except Exception as e:
    #         raise TablePriceError(e)

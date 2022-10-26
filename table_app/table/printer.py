from table_app.table.custom_error import *
class Printer(object):

    def __init__(self, app_plate):
        self.app_plate = app_plate
    #print table material and price

    def print_table(self, money):
        try:
            result = ""
            for i in self.app_plate:
                temp = ""
                for j in i:
                    xxx = getattr(j, money)
                    temp += str(xxx) + " "
                result += temp + '\n'
            print(result)
        except Exception as e:
            raise PrinterConfigError(e)

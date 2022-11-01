from table_app.table.custom_error import *


class TablePrinter(object):

    def __init__(self, template):
        self.template = template

    def print(self, param):
        """ print table material and price """
        try:
            result = ""
            for i in self.template:
                temp = ""
                for j in i:
                    xxx = getattr(j, param)
                    temp += str(xxx) + " "
                result += temp + '\n'
            print(result)
        except Exception as e:
            raise PrinterConfigError(e)

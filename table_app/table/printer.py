class Printer(object):

    def __init__(self, app_plate):
        self.app_plate = app_plate

    def print_table(self, money):
        result = ""
        for i in self.app_plate:
            temp = ""
            for j in i:
                xxx = getattr(j, money)
                temp += str(xxx) + " "
            result += temp + '\n'
        print(result)

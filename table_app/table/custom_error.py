class TableError(Exception):
    pass


class TableConfigError(TableError):
    pass


class TablePriceError(TableError):
    pass


class PrinterConfigError(TableError):
    pass

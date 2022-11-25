from abc import ABCMeta, abstractmethod
from six import with_metaclass
import random


class PrinterAbc(with_metaclass(ABCMeta)):

    @abstractmethod
    def result(self):
        pass


class AsciiPrinter(PrinterAbc):
    """print ascii style"""

    def __init__(self, info):
        self.info = info

    def result(self):
        """define correct phrase for print"""
        if self.info.print_points_errors is True:
            z = self.info.errors
            info = ''.join(self.info.hidden_word).capitalize()
            print(f'Word: {info}    , Left errors : {z} !!!')

        if self.info.print_win is True:
            print(f'Good game , you WIN !!!!!')
            self.info.print_win = False

        if self.info.print_lose is True:
            print(f'That`s bad , you lost the game !!!')
            self.info.print_lose = False

        if self.info.print_command_try is True:
            print("No enough hil_points !!!")
            self.info.print_command_try = False

        if self.info.take_hint is True:
            print('No enough points !!!')
            self.info.take_hint = False

        if self.info.show_wrong_chr is True:
            all_word = ", ".join(self.info.wrong_chr)
            print(f'Wrong suggestions: {all_word}')



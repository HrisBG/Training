from abc import ABCMeta, abstractmethod
from six import with_metaclass
import random


class PrinterAbc(with_metaclass(ABCMeta)):
    pass


class AsciiPrinter(PrinterAbc):

    def __init__(self, info):
        self.info = info

    def result(self):
        if self.info.print_points_errors is True:
            z = self.info.errors
            info = ''.join(self.info.hidden_word).capitalize()
            print(f'Word: {info}    ,Errors : {z} !!!')

    def win(self):
        if self.info.print_win is True:
            print(f'Good game , you WIN !!!!!')

    def lost_game(self):
        if self.info.print_lose is True:
            print(f'That`s bad , you lost the game !!!')

    def another_try(self):
        if self.info.print_command_try is True:
            print("No enough hil_points !!!")

    def take_hint(self):
        if self.info.take_hint is True:
            print('No enough points !!!')

    def show_wrong_suggestions(self):
        if self.info.show_wrong_chr is True:
            all_word = ", ".join(self.info.wrong_chr)
            print(f'Wrong suggestions: {all_word}')



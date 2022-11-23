from abc import ABCMeta, abstractmethod
from six import with_metaclass
import random


class PrinterAbc(with_metaclass(ABCMeta)):
    pass


class AsciiPrinter(PrinterAbc):

    @staticmethod
    def result(info):
        if info.print_points_errors is True:
            z = info.errors
            info = ''.join(info.hidden_word).capitalize()
            print(f'Word: {info} ,Errors : {z}')

    @staticmethod
    def win(info):
        if info.print_win is True:
            print(f'Good game , you WIN !!!!!')

    @staticmethod
    def lost_game(info):
        if info.print_lose is True:
            print(f'That`s bad , you lost the game')

    @staticmethod
    def another_try(info):
        if info.print_command_try is True:
            print("No enough hil_points")

    @staticmethod
    def take_hint(info):
        if info.take_hint is True:
            print('No enough points')

    @staticmethod
    def show_wrong_suggestions(info):
        if info.show is True:
            all_word = ", ".join(info.wrong_chr)
            print(f'Wrong suggestions: {all_word}')



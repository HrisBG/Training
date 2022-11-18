import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass


class VisualizationAbc(with_metaclass(ABCMeta)):
    pass


class AsciiVisualization(VisualizationAbc):
    """Contains all methods for printing"""

    @staticmethod
    def show_hidden_word(word):
        word = ''.join(word).capitalize()
        print(word)

    @staticmethod
    def greeting(name):
        print(f'Hi, {name}!!!!')

    @staticmethod
    def old_player(name):
        print(f'Welcome back {name} !!!!')

    @staticmethod
    def start_game():
        print('Let`s play Hangman')

    @staticmethod
    def errors(error):
        x = random.choice(['Bad suggestions:', 'Errors :', f'Number of tries! :'])
        print(f'{x} {error}')

    @staticmethod
    def make_suggestion():
        return 'Please make your suggestion: '

    @staticmethod
    def right_chr(letter):
        print(f'Yes, the --> {letter} <-- is in the word')

    @staticmethod
    def wrong_chr(letter):
        print(f'No, the --> {letter} <-- is not in word')

    @staticmethod
    def all_wrong_chr(letters):
        print(f'Wrong letters: {", ".join(letters)}')

    @staticmethod
    def last_try():
        print('Last try')

    @staticmethod
    def win(name):
        print(f'Good game {name}, you WIN !!!!!')

    @staticmethod
    def lost_game(name):
        print(f'That`s bad , {name}, you lost the game')

    @staticmethod
    def no_try():
        print(f'Not enough tries')

    @staticmethod
    def no_hil_points():
        print(f'Not enough HIL points')

    @staticmethod
    def add_try(points):
        print(f'You add 1 try !!!Now you have - {points} HIL points !!!')

    @staticmethod
    def show_hil_points(name, points):
        print(f"{name} , your HIL points are {points} !!!")

    @staticmethod
    def show_chr():
        return 'If you don`t want to see the wrong letters press --> N <-- ,' + '\n' + 'otherwise press any button: '

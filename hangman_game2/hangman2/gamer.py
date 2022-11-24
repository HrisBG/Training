from hangman_game2.hangman2.words_db import *
from hangman_game2.hangman2.player_db import *
import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass


class GamerAbc(with_metaclass(ABCMeta)):
    pass


class Player(GamerAbc):

    def __init__(self, hil_points=20):
        self.name = ''
        self.difficulty = ''
        self.category = ''
        self.hil_points = hil_points
        self.player_word = ''
        self.input_str = ''
        self.category_list = []
        self.params = (0, 0)
        self.temp_list = []

    def check_player(self):
        self.name = input('Hello , please write yor name: ')
        if self.name in PlayerDB.players:
            self.hil_points = PlayerDB.players[self.name]

    def get_difficulty(self):
        self.difficulty = input('Please choose you difficulty level /easy, normal , hard/ : ')
        all_type = {
            'easy': (3, 5),
            'normal': (6, 9),
            'hard': (10, 189819)
        }
        self.params = all_type[self.difficulty]
        return self

    def get_category_words(self):
        self.category = input('Please choose category /city, animal , sport/: ')
        category_list = getattr(WordsDB, self.category)
        self.category_list = category_list
        return self

    def get_temp_list(self):
        for i in self.category_list:
            if self.params[0] <= len(i) <= self.params[1]:
                self.temp_list.append(i.lower())
        return self

    def get_word(self):
        self.player_word = random.choice(self.temp_list)
        return self

    def input_chr(self):
        user_input = input("Please make your suggestion: ")
        self.input_str = user_input
        return self



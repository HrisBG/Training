from hangman_game2.hangman2.words_db import *
from hangman_game2.hangman2.player_db import *
import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass


class GamerAbc(with_metaclass(ABCMeta)):
    pass


class Player(GamerAbc):
    """Work with input data, check for saved player and define game word """

    def __init__(self, name, difficulty, category, hil_points=20):
        self.name = name
        self.difficulty = difficulty
        self.category = category
        self.hil_points = hil_points
        self.word = ''
        self.input_str = ''
        self.category_list = []
        self.params = (0, 0)
        self.temp_list = []

    def check_old_player(self):
        """check for saved player"""
        if self.name in PlayerDB.players:
            self.hil_points = PlayerDB.players[self.name]

    def get_difficulty(self):
        """define word parameters"""
        all_type = {
            'easy': (3, 5),
            'normal': (6, 9),
            'hard': (10, 189819)
        }
        self.params = all_type[self.difficulty]
        return self

    def get_category_words(self):
        """take all word for chosen category """
        category_list = getattr(WordsDB, self.category)
        self.category_list = category_list
        return self

    def get_temp_list(self):
        """select list of words"""
        new_list = []
        for i in self.category_list:
            if self.params[0] <= len(i) <= self.params[1]:
                new_list.append(i.lower())
        self.temp_list = new_list
        return self

    def get_word(self):
        """take random word"""
        self.get_difficulty()
        self.get_category_words()
        self.get_temp_list()
        self.word = random.choice(self.temp_list)
        return self

    def input_chr(self):
        """take player suggestions"""
        self.input_str = input("Please make your suggestion: ").lower()
        return self



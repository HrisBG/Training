from hangman_game2.hangman2.words_db import *
from hangman_game2.hangman2.player_db import *
import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass


class GamerAbc(with_metaclass(ABCMeta)):
    pass


class Player(GamerAbc):

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
        if self.name in PlayerDB.players:
            self.hil_points = PlayerDB.players[self.name]

    def get_difficulty(self):
        all_type = {
            'easy': (3, 5),
            'normal': (6, 9),
            'hard': (10, 189819)
        }
        self.params = all_type[self.difficulty]
        return self

    def get_category_words(self):
        category_list = getattr(WordsDB, self.category)
        self.category_list = category_list
        return self

    def get_temp_list(self):
        new_list = []
        for i in self.category_list:
            if self.params[0] <= len(i) <= self.params[1]:
                new_list.append(i.lower())
        self.temp_list = new_list
        return self

    def get_word(self):
        self.get_difficulty()
        self.get_category_words()
        self.get_temp_list()
        self.word = random.choice(self.temp_list)
        return self

    def input_chr(self):
        user_input = input("Please make your suggestion: ").lower()
        self.input_str = user_input
        return self



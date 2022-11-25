from hangman_game2.hangman2.commands import *


class GameLogic(object):

    def __init__(self, gamer):
        self.gamer = gamer
        self.name = gamer.name
        self.word = gamer.word
        self.hidden_word = None
        self.wrong_chr = []
        self.errors = 0
        self.show_wrong_chr = True
        self.game_run = True
        self.print_win = False
        self.print_lose = False
        self.print_points_errors = True
        self.print_command_try = False
        self.take_hint = False

        self.get_errors()

    def words_configurator(self):
        self.hidden_word = ('_' * len(self.gamer.word))
        self.hidden_word = [_ for _ in self.hidden_word]
        self.gamer.word = [_ for _ in self.gamer.word]
        return self

    def get_errors(self):
        self.errors = len(self.gamer.word)
        return self.errors

    def check_errors(self):
        if self.errors <= 0:
            self.print_lose = True
            self.game_run = False
            return self

    def check_word(self, input_word):
        temp_word = [_ for _ in input_word]
        if temp_word == self.gamer.word or self.hidden_word == self.gamer.word:
            self.gamer.hil_points += 1
            self.print_points_errors = False
            self.print_win = True
            self.show_wrong_chr = False
            self.game_run = False
        return self

    def show_wrong_suggestions(self):
        x = input('If you don`t want to see the wrong letters press --> N <-- ,' +
                  '\n' + 'otherwise press any button: ')

        if x == "n":
            self.show_wrong_chr = False

    def logic(self, player_info):

        if len(player_info.input_str) > 1:
            if player_info.input_str[0] == "@":
                c1 = Commands(self)
                c1.get_command(player_info.input_str)
            else:
                self.check_word(player_info.input_str)
            return self
        else:
            if player_info.input_str in self.gamer.word:
                for i in range(len(self.gamer.word)):
                    if player_info.input_str == self.gamer.word[i]:
                        self.hidden_word[i] = player_info.input_str
                        self.check_word(player_info.input_str)
            else:
                if player_info.input_str not in self.wrong_chr:
                    self.wrong_chr.append(player_info.input_str)
                self.errors -= 1
                self.check_errors()
            return self

    def check_game_run(self):
        return self

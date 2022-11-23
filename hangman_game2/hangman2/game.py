import random


class Game(object):

    def __init__(self, name, word, hil_points):
        self.name = name
        self.word = word
        self.hil_points = hil_points
        self.hidden_word = None
        self.wrong_chr = []
        self.errors = 0
        self.show = True
        self.game_run = True
        self.print_win = False
        self.print_lose = False
        self.print_points_errors = True
        self.print_command_try = False
        self.take_hint = False

        self.get_possible_errors()

    def words_configurator(self):
        self.hidden_word = ('_' * len(self.word))
        self.hidden_word = [_ for _ in self.hidden_word]
        self.word = [_ for _ in self.word]
        return self

    def get_possible_errors(self):
        self.errors = len(self.word)
        return self.errors

    def check_errors(self):
        if self.errors <= 0:
            self.print_lose = True
            self.game_run = False
            return self

    def check_hidden_and_word(self):
        if self.hidden_word == self.word:
            self.print_points_errors = False
            self.print_win = True
            self.game_run = False
        return self

    def check_input_str_and_word(self, letter):

        if letter.input_str == letter.player_word:
            self.print_points_errors = False
            self.print_win = True
            self.game_run = False
        return self

    def command_try(self, player_info):
        if self.hil_points < 10:
            self.print_command_try = True
        else:
            self.errors += 1
            self.hil_points -= 10
            return self

    def command_difficulty(self, player_info):

        player_info.get_difficulty()
        ll = []
        for i in player_info.category_list:
            if player_info.params[0] <= len(i) <= player_info.params[1]:
                ll.append(i.lower())
        player_info.temp_list = ll
        player_info.player_word = random.choice(player_info.temp_list)
        self.word = player_info.player_word
        self.words_configurator()
        self.get_possible_errors()
        return self

    def command_category(self, player_info):

        player_info.get_category_words()
        ll = []
        for i in player_info.category_list:
            if player_info.params[0] <= len(i) <= player_info.params[1]:
                ll.append(i.lower())
        player_info.temp_list = ll
        player_info.player_word = random.choice(player_info.temp_list)
        self.word = player_info.player_word
        self.words_configurator()
        self.get_possible_errors()
        return self

    def command_hint(self, player_info):
        temp_errors = self.errors
        self.errors -= 2

        if self.errors <= 0:
            self.errors = temp_errors
            self.take_hint = True
        else:
            for i in range(len(self.word)):
                self.word = [_ for _ in self.word]
                if self.hidden_word[i] != self.word[i]:
                    self.hidden_word[i] = self.word[i]
                    break
        return self

    def command_stop(self, player_info):
        self.print_points_errors = False
        self.game_run = False
        return self

    def get_command(self, command, player_info):
        commands = {
            '@try': self.command_try,
            '@stop': self.command_stop,
            '@difficulty': self.command_difficulty,
            '@category': self.command_category,
            '@hint': self.command_hint
        }

        command_type = commands[command]
        return command_type(player_info)

    def show_wrong_suggestions(self):
        x = input("'If you don`t want to see the wrong letters press --> N <-- ,"
                  "' + '\n' + 'otherwise press any button: '")
        if x == "N":
            self.show = False

    def logic(self, player_info):

        if len(player_info.input_str) > 1:
            if player_info.input_str[0] == "@":
                self.get_command(player_info.input_str, player_info)
            else:
                self.check_input_str_and_word(player_info)
            return self
        else:
            if player_info.input_str in self.word:
                for i in range(len(self.word)):
                    if player_info.input_str == self.word[i]:
                        self.hidden_word[i] = player_info.input_str
                        self.check_hidden_and_word()
            else:
                if player_info.input_str not in self.wrong_chr:
                    self.wrong_chr.append(player_info.input_str)
                self.errors -= 1
                self.check_errors()
            return self

    def check_game_run(self):
        return self

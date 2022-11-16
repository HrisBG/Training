from hangman_game.hangman.asciivisualization import *
from hangman_game.hangman.players import *
from hangman_game.hangman.words import *
from abc import ABCMeta, abstractmethod
from six import with_metaclass

player_name = input('Please insert your name:').capitalize()
player_difficulty = input('Choose difficult - easy,normal or hard:')
player_category = input('Choose category - city, animal or sport:')
# player_name = 'Peter'
# player_category = 'city'
# player_difficulty = 'easy'


class GameAbc(with_metaclass(ABCMeta)):

    @abstractmethod
    def run_game(self):
        pass

    @abstractmethod
    def start_game_engine(self):
        pass

    @abstractmethod
    def check_input_chr(self):
        pass


class Game(GameAbc):

    def __init__(self, name, category, difficulty):
        self.player_name = name
        self.category = category
        self.difficulty = difficulty
        self.show_wrong_letter = True
        self.hil_points = 0
        self.input_chr = None
        self.wrong_chr = []
        self.game_on = True
        self.params = (0, 0)
        self.category_list = []
        self.temp_list = []
        self.player_word = ''
        self.errors = None
        self.play = True
        self.exit = False
        self.hidden_word = None
        self.commands = {}

        # check player name from list or add new player
        if player_name in PlayerDB.players:
            self.hil_points = PlayerDB.players[player_name]

        self.define_difficulty_param()
        self.get_list()
        self.get_temp_list()

    def get_list(self):
        """get list of selected category"""
        category_list = getattr(WordsDB, self.category)
        self.category_list = category_list

    def define_difficulty_param(self):

        """take parameters of selected difficulty"""
        all_type = {
            'easy': (3, 5),
            'normal': (6, 9),
            'hard': (10, 189819)
        }
        self.params = all_type[self.difficulty]

    def get_temp_list(self):
        """return list with possible words"""
        ll = []
        for i in self.category_list:
            if self.params[0] <= len(i) <= self.params[1]:
                ll.append(i.lower())
        self.temp_list = ll

    def get_player_word(self):
        """get player word from temporary list"""

        word = random.choice(self.temp_list)  # Fixme: try catch if empty
        self.temp_list.remove(word)           # TODO: repair
        return word

    def get_possible_errors(self):
        return len(self.player_word)

    def check_errors(self):
        if self.errors <= 0:
            return False

    def show_letters(self):
        """switch off the collection of guess letters"""
        choose = input(AsciiVisualization.show_chr()).lower()
        if choose == 'n':
            self.show_wrong_letter = False

    def words_configurator(self):
        """make hidden word"""
        self.hidden_word = ('_' * len(self.player_word))
        self.hidden_word = [_ for _ in self.hidden_word]
        self.player_word = [_ for _ in self.player_word]
        return

    def command_try(self):
        """gain one try if player have enough HIL points"""
        if self.hil_points <= 10:
            AsciiVisualization.no_hil_points()
            return
        else:
            self.errors += 1
            self.hil_points -= 10
            AsciiVisualization.add_try(self.hil_points)
            return

    def command_difficulty(self):
        """change difficulty level"""
        self.difficulty = input('Choose difficulty - easy,normal or hard: ')
        self.get_list()
        self.define_difficulty_param()
        self.get_temp_list()
        self.game_on = False
        return

    def command_category(self):
        """change category"""
        self.category = input('Choose category - city, animal or sport: ')
        self.get_list()
        self.define_difficulty_param()
        self.get_temp_list()
        self.game_on = False
        return

    def command_hint(self):
        temp_errors = self.errors
        self.errors -= 2
        if self.check_errors() is False:
            AsciiVisualization.no_try()
            self.errors = temp_errors
        else:
            for i in range(len(self.player_word)):
                self.player_word = [_ for _ in self.player_word]
                if self.hidden_word[i] != self.player_word[i]:
                    self.hidden_word[i] = self.player_word[i]
                    break
        return

    def command_stop(self):
        self.game_on = False
        return

    def command_exit(self):
        self.game_on = False
        self.exit = True
        return

    def get_command(self, command):
        self.commands = {
            'try': self.command_try,
            'stop': self.command_stop,
            'exit': self.command_exit,
            'difficulty': self.command_difficulty,
            'category': self.command_category,
            'hint': self.command_hint
        }

        command_type = self.commands[command]
        return command_type()

    def check_input_chr(self):
        """check suggestion letter is right or not"""
        if self.input_chr in self.player_word:
            for i in range(len(self.player_word)):
                if self.input_chr == self.player_word[i]:
                    self.hidden_word[i] = self.input_chr
            AsciiVisualization.right_chr(self.input_chr)

            if self.player_word == self.hidden_word:
                self.hil_points += 1
                AsciiVisualization.win(self.player_name)
                AsciiVisualization.show_hil_points(self.player_name, self.hil_points)
                self.game_on = False
        else:
            if self.input_chr not in self.wrong_chr:
                self.wrong_chr.append(self.input_chr)
            AsciiVisualization.wrong_chr(self.input_chr)

            if self.show_wrong_letter is True:
                AsciiVisualization.all_wrong_chr(self.wrong_chr)
            self.errors -= 1
            AsciiVisualization.errors(self.errors)

    def start_game_engine(self):
        """
        check user input for command , suggestion letter or whole word and
        check player points
        """
        AsciiVisualization.start_game()
        AsciiVisualization.show_hil_points(self.player_name, self.hil_points)
        self.words_configurator()
        self.show_letters()
        while self.game_on is not False:
            AsciiVisualization.show_hidden_word(self.hidden_word)

            self.input_chr = input(AsciiVisualization.make_suggestion()).lower()

            # check type of input
            if len(self.input_chr) > 1:
                if self.input_chr[0] == '@':
                    command = self.input_chr[1:]
                    self.get_command(command)
                    continue

                # check whole word suggestion
                temp_input_chr = self.input_chr = [_ for _ in self.input_chr]
                if temp_input_chr == self.player_word:
                    self.hil_points += 1
                    AsciiVisualization.win(self.player_name)
                    AsciiVisualization.show_hil_points(self.player_name, self.hil_points)
                    break
                else:
                    if self.input_chr not in self.wrong_chr:
                        self.wrong_chr.append(self.input_chr)
                    AsciiVisualization.wrong_chr(self.input_chr)
                    self.errors -= 1
                    AsciiVisualization.errors(self.errors)
                    continue

            self.check_input_chr()

            # check points for continue game
            if self.check_errors() is False:
                AsciiVisualization.lost_game(self.player_name)
                self.game_on = False

    def run_game(self):
        """start , restart and close game"""
        AsciiVisualization.greeting(self.player_name)

        while self.play is True:
            self.player_word = self.get_player_word()
            self.errors = self.get_possible_errors()
            self.wrong_chr = []
            self.start_game_engine()

            if self.exit is True:
                break

            game = input("Play Again ?" + '\n' + 'Y / N : ').lower()

            if game == 'y':
                self.play = True
                self.game_on = True
            else:
                self.play = False


player1 = Game(player_name, player_category, player_difficulty)
player1.run_game()

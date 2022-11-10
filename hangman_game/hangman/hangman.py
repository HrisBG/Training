from hangman_game.hangman.visualization import *
from hangman_game.hangman.players import *
from hangman_game.hangman.words import *

# player_name = input('Please insert your name:')
# player_difficulty = input('Choose difficult - easy,normal or hard:')
# player_category = input('Choose category - city, animal or sport:')


player_name = 'Peter'
player_category = 'city'
player_difficulty = 'easy'


class Game(object):

    def __init__(self, name, category, difficulty):
        self.player_name = name
        self.category = category
        self.difficulty = difficulty
        self.show_wrong_letter = False
        self.hil_points = 0
        self.suggestion_letter = None
        self.wrong_letters = []
        self.game_on = True
        self.params = (0, 0)
        self.category_list = []
        self.temp_list = []
        self.player_word = ''
        self.points = None
        self.play = True
        self.exit = False
        self.hidden_word = None

        # check player name from list or add new player
        if player_name in PlayerDB.players:
            self.hil_points = PlayerDB.players[player_name]

        self.difficulty_param()
        self.get_list()
        self.get_temp_list()

    def get_list(self):
        """get list of selected category"""
        category_list = getattr(WordsDB, self.category)
        self.category_list = category_list

    def difficulty_param(self):
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
        word = random.choice(self.temp_list)
        self.temp_list.remove(word)
        return word

    def player_points(self):
        return len(self.player_word)

    def check_points(self):
        if self.points <= 0:
            return False

    def show_letters(self):
        """switch on or off the collection of guess letters"""
        choose = input('If you want to see the wrong letters , press -  Y : ').lower()
        if choose == 'y':
            self.show_wrong_letter = True

    def command_try(self):
        """gain one try if player have enough HIL points"""
        if self.hil_points < 10:
            Visualization.no_hil_points()
            return
        else:
            self.points += 1
            self.hil_points -= 10
            Visualization.add_try(self.hil_points)
            return

    def command_difficulty(self):
        """change difficulty level"""
        self.difficulty = input('Choose difficulty - easy,normal or hard: ')
        self.get_list()
        self.difficulty_param()
        self.get_temp_list()
        return

    def command_category(self):
        """change category"""
        self.category = input('Choose category - city, animal or sport: ')
        self.get_list()
        self.difficulty_param()
        self.get_temp_list()
        return

    def hidden_word_configurator(self):
        """make hidden word"""
        self.hidden_word = ('_' * len(self.player_word))
        self.hidden_word = [_ for _ in self.hidden_word]
        return

    def hint_logic(self):
        """open one hidden letter in hidden word"""
        for i in range(len(self.player_word)):
            self.player_word = [_ for _ in self.player_word]
            if self.hidden_word[i] != self.player_word[i]:
                self.hidden_word[i] = self.player_word[i]
                self.player_word = ''.join(self.player_word)
            break
        return

    def game_engine_logic(self):
        """check suggestion letter is right or not"""
        if self.suggestion_letter in self.player_word:
            for i in range(len(self.player_word)):
                if self.suggestion_letter == self.player_word[i]:
                    self.hidden_word[i] = self.suggestion_letter
            Visualization.right_letter(self.suggestion_letter)
            if self.player_word == ''.join(self.hidden_word):
                Visualization.win(self.player_name)
                self.hil_points += 1
                self.game_on = False
        else:
            if self.suggestion_letter not in self.wrong_letters:
                self.wrong_letters.append(self.suggestion_letter)
            Visualization.wrong_letter(self.suggestion_letter)
            if self.show_wrong_letter is True:
                Visualization.all_wrong_letters(self.wrong_letters)
            self.points -= 1
            Visualization.score(self.points)

    def game_engine(self):
        """
        check user input for command , suggestion letter or whole word and
        check player points
        """
        Visualization.start_game()
        self.hidden_word_configurator()
        self.show_letters()
        while self.game_on is not False:
            Visualization.show_hidden_word(self.hidden_word)
            self.suggestion_letter = input(Visualization.make_suggestion()).lower()
#           check type of input
            if self.suggestion_letter[0] == '@':
                command = self.suggestion_letter[1:]
#               check type of command
                if command == "try":
                    self.command_try()
                    self.suggestion_letter = input(Visualization.make_suggestion()).lower()
                if command == 'stop' or command == "exit":
                    if command == "exit":
                        self.exit = True
                    break
                if command == 'difficulty':
                    self.command_difficulty()
                    break
                if command == 'category':
                    self.command_category()
                    break
                if command == 'hint':
                    self.points -= 2
                    if self.check_points() is False:
                        Visualization.no_points()
                    else:
                        self.hint_logic()
                        continue
#           check whole word suggestion
            if len(self.suggestion_letter) > 0 and self.suggestion_letter[0] != "@" and \
                    self.suggestion_letter == self.player_word:
                self.hil_points += 1
                Visualization.win(self.player_name)
                break
            self.game_engine_logic()
            # if self.suggestion_letter in self.player_word:
            #     for i in range(len(self.player_word)):
            #         if self.suggestion_letter == self.player_word[i]:
            #             self.hidden_word[i] = self.suggestion_letter
            #     Visualization.right_letter(self.suggestion_letter)
            #     if self.player_word == ''.join(self.hidden_word):
            #         Visualization.win(self.player_name)
            #         self.hil_points += 1
            #         self.game_on = False
            # else:
            #     if self.suggestion_letter not in self.wrong_letters:
            #         self.wrong_letters.append(self.suggestion_letter)
            #     Visualization.wrong_letter(self.suggestion_letter)
            #     if self.show_wrong_letter is True:
            #         Visualization.all_wrong_letters(self.wrong_letters)
            #     self.points -= 1
            #     Visualization.score(self.points)
#           check points for continue game
            if self.check_points() is False:
                Visualization.lost_game(self.player_name)
                self.game_on = False

    def run(self):
        """start , restart and close game"""
        Visualization.greeting(self.player_name)
        while self.play is True:
            self.player_word = self.get_player_word()
            self.points = self.player_points()
            self.wrong_letters = []
            self.game_engine()
            if self.exit is True:
                break
            game = input("Play Again ?" + '\n' + 'Y / N : ').lower()
            if game == 'y':
                self.play = True
                self.game_on = True
            else:
                self.play = False


g1 = Game(player_name, player_category, player_difficulty)
g1.run()

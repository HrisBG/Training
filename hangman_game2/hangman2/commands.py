from hangman_game2.hangman2.custom_error import *
class Commands(object):
    """all special commands """
    def __init__(self, data):
        self.data = data

    def gives_try(self):
        """gives another suggestions"""
        if self.data.gamer.hil_points < 10:
            self.data.print_command_try = True
        else:
            self.data.errors += 1
            self.data.gamer.hil_points -= 10
            return self

    def change_difficulty(self):
        """change old difficulty with new"""
        new_difficulty = input("new difficulty: ")
        self.data.gamer.difficulty = new_difficulty
        self.data.gamer.get_word()
        self.data.words_configurator()
        self.data.get_errors()
        return self

    def change_category(self):
        """change old category with new"""
        new_category = input("new_category: ")
        self.data.gamer.category = new_category
        self.data.gamer.get_word()
        self.data.words_configurator()
        self.data.get_errors()
        return self

    def gives_hint(self):
        """gives hint, open 1 letter """
        temp_errors = self.data.errors
        self.data.errors -= 2

        # check for enough errors for hint
        if self.data.errors <= 0:
            self.data.errors = temp_errors
            self.data.take_hint = True

        else:
            for i in range(len(self.data.gamer.word)):
                self.data.gamer.word = [_ for _ in self.data.gamer.word]
                if self.data.hidden_word[i] != self.data.gamer.word[i]:
                    self.data.hidden_word[i] = self.data.gamer.word[i]
                    break
        return self

    def stop_game(self):
        """quit game"""
        self.data.print_points_errors = False
        self.data.game_run = False
        return self

    def get_command(self, command):
        """define player command"""
        try:
            commands = {
                '@try': self.gives_try,
                '@stop': self.stop_game,
                '@difficulty': self.change_difficulty,
                '@category': self.change_category,
                '@hint': self.gives_hint
            }

            command_type = commands[command]
        except Exception:
            raise DifficultyError('wrong command')
        return command_type()

class Commands(object):

    def __init__(self, data):
        self.data = data

    def command_try(self):
        if self.data.gamer.hil_points < 10:
            self.data.print_command_try = True
        else:
            self.data.errors += 1
            self.data.gamer.hil_points -= 10
            return self

    def command_difficulty(self):
        new_difficulty = input("new difficulty: ")
        self.data.gamer.difficulty = new_difficulty
        self.data.gamer.get_word()
        self.data.words_configurator()
        self.data.get_errors()
        return self

    def command_category(self):
        new_category = input("new_category: ")
        self.data.gamer.category = new_category
        self.data.gamer.get_word()
        self.data.words_configurator()
        self.data.get_errors()
        return self

    def command_hint(self):
        temp_errors = self.data.errors
        self.data.errors -= 2

        if self.data.errors <= 0:
            self.data.errors = temp_errors
            self.data.take_hint = True
        else:
            for i in range(len(self.data.word)):
                self.data.word = [_ for _ in self.data.word]
                if self.data.hidden_word[i] != self.data.word[i]:
                    self.data.hidden_word[i] = self.data.word[i]
                    break
        return self

    def command_stop(self):
        self.data.print_points_errors = False
        self.data.game_run = False
        return self

    def get_command(self, command):
        commands = {
            '@try': self.command_try,
            '@stop': self.command_stop,
            '@difficulty': self.command_difficulty,
            '@category': self.command_category,
            '@hint': self.command_hint
        }

        command_type = commands[command]
        return command_type()

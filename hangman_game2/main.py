from hangman2.input_status import *
from hangman2.game import *
from hangman2.printer import *


data = InputStatus()
data.check_player()
data.get_difficulty()
data.get_category_words()
data.get_temp_list()
data.get_word()

game = Game(data.name, data.player_word, data.hil_points)
game.words_configurator()

printer = AsciiPrinter()

print(data.name, data.player_word, data.hil_points)
print(''.join(game.hidden_word))

game_run = True

while game.game_run:
    game_run = True
    player_info = data.input_chr()

    game_data = game.logic(player_info)
    check = game.check_game_run()

    printer.result(game_data)
    printer.win(game_data)
    printer.lost_game(game_data)
    printer.another_try(game_data)
    printer.take_hint(game_data)
    printer.show_wrong_suggestions(game_data)


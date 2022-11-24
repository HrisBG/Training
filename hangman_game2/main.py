from hangman2.input_status import *
from hangman2.game import *
from hangman2.printer import *


player = Player()
player.check_player()
player.get_difficulty()
player.get_category_words()
player.get_temp_list()
player.get_word()

game = GameLogic(player.name, player.player_word, player.hil_points)
game.words_configurator()

printer = AsciiPrinter()

print(player.name, player.player_word, player.hil_points)
print(''.join(game.hidden_word))

game_run = True

while game.game_run:
    game_run = True
    player_info = player.input_chr()

    game_data = game.logic(player_info)
    check = game.check_game_run()

    printer.result(game_data)
    printer.win(game_data)
    printer.lost_game(game_data)
    printer.another_try(game_data)
    printer.take_hint(game_data)
    printer.show_wrong_suggestions(game_data)


from hangman2.gamer_info import *
from hangman2.game_logic import *
from hangman2.printer import *


name = input('Please insert your name: ')
difficulty = input('Choose difficult - easy,normal or hard: ')
category = input('Choose category - city, animal or sport: ')

player = Player(name, difficulty, category)
player.get_word()

game = GameLogic(player)
game.words_configurator()

printer = AsciiPrinter(game)

print(player.name, player.word, player.hil_points)

print(''.join(game.hidden_word))

game.show_wrong_suggestions()

while game.game_run:

    player_input = player.input_chr()

    game_run = game.logic(player_input)
    check = game.check_game_run()

    printer.result()
    printer.show_wrong_suggestions()
    printer.win()
    printer.lost_game()
    printer.another_try()
    printer.take_hint()


print(player.hil_points)

from hangman2.gamer_info import *
from hangman2.game_logic import *
from hangman2.printer import *


name = input('Please insert your name: ')
difficulty = input('Choose difficult - easy,normal or hard: ')
category = input('Choose category - city, animal or sport: ')

player = Player(name, difficulty, category)
try:
    player.get_word()
except CategoryError as e:
    print(e)

game = GameLogic(player)
game.words_configurator()

printer = AsciiPrinter(game)

print('Word: ' + (''.join(game.hidden_word)))

game.show_wrong_suggestions()

while game.game_run:

    player_input = player.input_chr()

    game_run = game.logic(player_input)
    check = game.check_game_run()

    printer_check = printer.result()


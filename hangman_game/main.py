from hangman.hangman import *

try:
    player1 = Game(player_name, player_category, player_difficulty)
    player1.run_game()
except DifficultyError as e:
    print(e)
except CategoryError as e:
    print(e)

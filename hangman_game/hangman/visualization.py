import random


class Visualization(object):

    @staticmethod
    def show_hidden_word(word):
        word = ''.join(word).capitalize()
        print(word)

    @staticmethod
    def greeting(name):
        print(f'Hi, {name}!!!!')

    @staticmethod
    def old_player(name):
        print(f'Welcome back {name} !!!!')

    @staticmethod
    def start_game():
        print('Let`s play Hangman')

    @staticmethod
    def score(points):
        x = random.choice(['The points is:', 'The Pooooints :', 'Left points :'])
        print(f'{x} {points}')

    @staticmethod
    def make_suggestion():
        return 'Please make your suggestion: '

    @staticmethod
    def right_letter(letter):
        print(f'Yes, the --> {letter} <-- is in the word')

    @staticmethod
    def wrong_letter(letter):
        print(f'No, the --> {letter} <-- is not in word')

    @staticmethod
    def all_wrong_letters(letters):
        print(f'Wrong letters: {", ".join(letters)}')

    @staticmethod
    def last_try():
        print('Last try')

    @staticmethod
    def win(name):
        print(f'Good game {name}, you WIN !!!!!')

    @staticmethod
    def lost_game(name):
        print(f'That`s bad , {name}, you lost the game')

    @staticmethod
    def no_points():
        print(f'Not enough points')

    @staticmethod
    def no_hil_points():
        print(f'Not enough HIL points')

    @staticmethod
    def add_try(points):
        print(f'You add 1 try !!!Now you have - {points} HIL points !!!')

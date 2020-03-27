"""
This is a lottery simulation game
written by: Aman Thakur

"""

import random


class Lottery:
    acc = 0
    stake = 0
    luck_draw = 0

    def _init_(self, stake, luck_draw, acc):
        self.stake = stake
        self.luck_draw = luck_draw
        self.acc = acc

    def gamble_by_own(self):
        self.stake = int(input('Enter the number between (1-10):'))
        self.luck_draw = random.randint(1, 10)
        if self.stake == self.luck_draw:
            self.acc += 900
        else:
            self.acc -= 100
        self.display_game_status()
        return self.stake, self.luck_draw

    def gamble(self):
        self.stake = random.randint(1, 10)
        self.luck_draw = random.randint(1, 10)
        if self.stake == self.luck_draw:
            self.acc += 900
        else:
            self.acc -= 100
        self.display_game_status()
        return self.stake, self.luck_draw

    def display_game_status(self):
        print('Bet=', self.stake)
        print('Luck Draw=', self.luck_draw)
        print('Your account in game =', self.acc)

    def play(self, i):
        c = int(input('Wish to play by your own enter 1 else enter 0 :'))
        if c == 1:
            self.stake, self.luck_draw = self.gamble_by_own()
        elif c == 0:
            self.stake, self.luck_draw = self.gamble()
        else:
            print('Enter the wrong choice!!')
            f = int(input('Wish to continue enter 1 if wish to continue else enter 0 :'))
            if f == 1:
                self.play()
            elif f == 0:
                print('This chance ', i, 'is skipped !!!')
                return


def rules_of_the_game():
    """ The rules of the game is very simple that you have to tell how much time you wish to play
        the computer will generate both the bet value and the lucky draw value randomly if you wins
        you will going to earn $900 i.e 10 folds of bet value otherwise loose $100 of yours!!!!!

        INSTANTLY MAKE MONEY AND BECOME RICH CHOICE YOURS!!!"""


def play_game():
    print('***********************************************************************************************************')
    print(rules_of_the_game.__doc__)
    print('***********************************************************************************************************')
    i = 0
    p = Lottery()

    n = int(input('Enter the number of times you wish to gamble:'))
    while i < n:
        print("***************************************************************************************************")
        print("                                       GAME:", i + 1, "                                              ")
        print("***************************************************************************************************")
        p.play(i+1)
        i += 1

    print('***********************************************************************************************************')
    if p.acc > 0:
        print('You earned a jackpot!!!')
    else:
        print('Better luck next time!!')
    print('Your account=', p.acc)
    print('***********************************************************************************************************')


if __name__ == "__main__":
    play_game()

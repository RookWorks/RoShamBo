# !/usr/bin/env python3
import random
# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

# """The Player class is the parent class for all of the Players
# in this game"""


class Player:

    def __init__(self):
        self.player_move = random.choice(moves)
        self.comp_move = random.choice(moves)

    # def move(self, player_move, comp_move):
    #     self.player_move = self.move
    #     self.comp_move = random.choice(self.move)

    def learn(self, player_move, comp_move):
        pass


class humanPlayer(Player):
    def move(self):
        while True:
            player_move = input('\033[1m' + "ROCK! PAPER! SCISSORS! "
                                "GO!\n" + '\033[0m').lower()
            if player_move in moves:
                return player_move
            else:
                print("Uh oh, that is not a move!")


# always picks rock
class rockPlayer(Player):
    def move(self):
        return 'rock'


# picks random
class randomPlayer(Player):
    def move(self):
        return random.choice(moves)


# mirrors the player
class reflectPlayer(Player):
    def move(self):
        return self.comp_move

    def learn(self, player_move, comp_move):
        self.player_move = player_move
        self.comp_move = comp_move


# always something different
class cyclePlayer(Player):
    def move(self):
        # print(self.comp_move)
        if self.comp_move == "scissors":
            self.comp_move = "rock"
            return "rock"
        elif self.comp_move == "rock":
            self.comp_move = "paper"
            return "paper"
        elif self.comp_move == "paper":
            self.comp_move = "scissors"
            return "scissors"


class Game:
    # Keeping score
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 == move2:
            print('\033[1m' + "TIE!\n" + '\033[0m')
        elif self.beats(move1, move2):
            self.p1_score += 1
            print('\033[1m' + "Score for you!\n" + '\033[0m')
        else:
            self.p2_score += 1
            print('\033[1m' + "Sorry you lost this round...\n" + '\033[0m')

        print('\033[1m' + f"Player 1: {move1}"
              f" Computer: {move2}\n" + '\033[0m')
        print('\033[1m' + f"Player 1: {self.p1_score}"
              f" Computer: {self.p2_score}\n" + '\033[0m')

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print('\033[1m' + "Are ya ready?! Let's go!\n" + '\033[0m')
        for round in range(3):
            print('\033[1m' + f"Round {round}:\n" + '\033[0m')
            self.play_round()
        if self.p1_score > self.p2_score:
            print('\033[1m' + "You won!\n" + '\033[0m')
            print('\033[1m' + "Final scores!\n" + '\033[0m')
            print('\033[1m' + f"Player: {self.p1_score} "
                  f"Computer: {self.p2_score}\n" + '\033[0m')
        elif self.p1_score < self.p2_score:
            print('\033[1m' + "You lost...\n" + '\033[0m')
            print('\033[1m' + "Final scores...\n" + '\033[0m')
            print('\033[1m' + f"Player: {self.p1_score}"
                  f" Computer: {self.p2_score}\n" + '\033[0m')
        else:
            print('\033[1m' + "It's a tie!" + '\033[0m')
        play_again()


def play_again():
    again = input('\033[1m' + "Would you like to try one more time? "
                  "(y/n) \n" + '\033[0m').lower()
    if again == "n":
        print('\033[1m' + "See ya!\n" + '\033[0m')
        exit(0)
    elif again == "y":
        print('\033[1m' + "Here we go!\n" + '\033[0m')
        game.play_game()
    else:
        print('\033[1m' + "I'm sorry what do you mean?\n" + '\033[0m')
        play_again()

if __name__ == '__main__':
    while True:
        players = [
                    rockPlayer(),
                    randomPlayer(),
                    reflectPlayer(),
                    cyclePlayer()
                    ]
        p1 = humanPlayer()
        p2 = random.choice(players)
        game = Game(p1, p2)
        game.play_game()

# Pycodestyle wants something here?

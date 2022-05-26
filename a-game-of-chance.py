"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random


moves = random.choice(['rock', 'paper', 'scissors'])
"""The Player class is the parent class for all of the Players
in this game"""


class Player(moves):
    def __init__(self):
        self.player1 = self.moves
        self.player2 = random.choice(self.moves)

    def learn(self, player1, player2):
        self.player2 = player2
        self.player1 = player1


class playerplayer(Player):
    def move(self):
        return self.player1

class compplayer(Player):
    def move(self):
        return random.choice(self.moves)

def beats(player1, player2):
    return ((player1 == 'rock' and player2 == 'scissors') or
            (player1 == 'scissors' and player2 == 'paper') or
            (player1 == 'paper' and player2 == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, moves):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    
game.play_game(moves)
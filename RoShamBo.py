#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    
    def __init__(self):
        self.player_move = random.choice(moves)
        self.comp_move = random.choice(moves)
    
    def move(self):
        self.player_move = self.move
        self.comp_move = random.choice(self.move)

    def learn(self, player_move, comp_move):
        self.player_move = player_move
        self.comp_move = comp_move

class humanPlayer(Player):
    def move(self):
        while True:
            player_move = input("ROCK! PAPER! SCISSORS! GO!\n").lower()
            if player_move in moves:
                return player_move

# picks random
class randomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
    
#mirrors the player    
class reflectPlayer(Player):
    def move(self):
        return self.comp_move
    
#always something different
class cyclePlayer(Player):
    def move(self):
        self.comp_move = random.sample(moves)
        return (self.comp_move)


class Game:
    #Keeping score
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

        print(f"Player 1: {move1}  Player 2: {move2}")
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Are ya ready?! Let's go!")
        for round in range(3,1):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(humanPlayer(), random.choice([randomPlayer(), reflectPlayer(), cyclePlayer()]))
    game.play_game()

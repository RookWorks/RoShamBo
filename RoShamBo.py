#!/usr/bin/env python3
import random
# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

# """The Player class is the parent class for all of the Players
# in this game"""


class Player:
    score = 0
    
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
        if self.my_move == moves[0]:
            return moves[1]
        elif self.comp_move == moves[1]:
            return moves[2]
        elif self.my_move == moves[2]:
            return moves[0]
        else: 
            return random.choice(moves)


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
        if move1 == move2:
            return ("TIE!\n")
        elif self.beats(move1, move2):
            self.p1_score += 1
            print("Score for you!\n")
        else:
            self.p2_score += 1
            print("Sorry you lost this round...\n")
        print(f"Player 1: {move1}  Computer: {move2}\n")
        print(f"Player 1: {self.p1_score} Computer: {self.p2_score}\n")
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        

    def play_game(self):
        print("Are ya ready?! Let's go!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("You won!\n")
            print("Final scores!\n")
            print(f"Player: {self.p1_score} Computer: {self.p2_score}\n")
        elif self.p1_score < self.p2_score:
            print("You lost...\n")
            print("Final scores...\n")
            print(f"Player: {self.p1_score} Computer: {self.p2_score}\n")
        else:
            print("It's a tie!")
        play_again()
        

def play_again():
    again = input("Would you like to try one more time? (y/n) \n").lower()
    if again == "y":
        print("Here we go!\n")
        game.play_game()
    elif again == "n":
        print("See ya!\n")
        quit()
    else:
        play_again()

if __name__ == '__main__':
    game = Game(humanPlayer(), random.choice([randomPlayer(), reflectPlayer(), cyclePlayer()]))
    game.play_game()

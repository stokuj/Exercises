# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) == len(player2_word):
            return 0
        elif len(player1_word) > len(player2_word):
            return 1
        else:
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        
        text1 = ''.join(char for char in player1_word if char in ['a','e','u','i','o'])
        text2 = ''.join(char for char in player2_word if char in ['a','e','u','i','o'])
        
        if len(text1) == len(text2):
            return 0
        elif len(text1) > len(text2):
            return 1
        else:
            return 2
        
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = ['rock', 'paper', 'scissors']
        if player1_word not in valid_moves and player2_word not in valid_moves:
            return 0
        
        # 2. Check if player 1 is invalid (Player 2 wins)
        if player1_word not in valid_moves:
            return 2
        
        # 3. Check if player 2 is invalid (Player 1 wins)
        if player2_word not in valid_moves:
            return 1
        
        if player1_word == player2_word:
            return 0
        elif player1_word == 'rock' and player2_word == 'scissors' or player1_word == 'paper' and player2_word == 'rock' or player1_word == 'scissors' and player2_word == 'paper':
            return 1
        else:
            return 2

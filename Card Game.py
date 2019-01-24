# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:21:08 2019

@author: Aakash Jha
"""

'''
Rules:
I am simulating the game of 21 (card game)
The first player to score 21 points wins the game.
Ace spades hearts or clubs have no role in the game of 21
If the player go beyond the score of 21 then his/her points is decremented by 10 points
This can be a 2 player game or a 4 player game.
'''

import random

List1 = ["A", "J", "K", "Q"]
Deck = []
for x in range(0, 4):
    for y in range(2, 11):
        Deck.append(y)
    for z in List1:
        Deck.append(z)

random.shuffle(Deck)


class Player:
    def __init__(self):
        self.hand = []
        self.score = setScore()
        self.name = setName()

    def pickacard(self):
        # shuffles the card and the player picks up the first card
        random.shuffle(Deck)
        hand.append(Deck[0])

        # removes the card from the deck when the player picks it up
        del (Deck[0])

    def setName(self):
        Name = input("Enter the player Name: ")
        return Name

    def getName(self):
        print(name)

    def getHand(self):
        print(hand)

    def getScore(self):
        print(score)

    def setScore(self):
        Score = 0
        List1dict = {"A": 11, "J": 10, "K": 10, "Q": 10}
        for cards in hand:
            if cards in range(2, 11):
                Score += cards
            elif cards in List1dict:
                Score += List1dict[cards]
        if (Score > 21):
            Score -= 10
        return Score


# A function to simulate the game

def game():
    player1 = Player
    player2 = Player
    player1.setName()
    player2.setName()
    while (True):

        print("It's " + Player1.name + " turn")
        Player1.pickacard()
        Player1.setScore()
        print("It's " + Player2.name + " turn")
        Player2.pickacard()
        Player2.setScore()
        if (player1.score == 21):
            print("The winner is " + player1.name)
            break
        elif (player2.score == 21):
            print("The winner is " + player2.name)
            break


game()






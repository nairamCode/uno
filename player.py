import random
from draw_card import draw_card

class player:
    def player_choose():
        global player1, player2, player3, player4, player_amount
        player_amount = input("Wie viele Spieler wollen mitspielen? (2-4): ")
        print(player_amount)
        player1 = []
        player2 = []
        player3 = []
        player4 = []
        if player_amount == "2":
            print("You selected 2 Players")
        elif player_amount == "3":
            print("You selected 3 Players")
        elif player_amount == "4":
            print("You selected 4 Players")
        else:
            player_amount = input("Wie viele Spieler wollen mitspielen? (max. 4): ")
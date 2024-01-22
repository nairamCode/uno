import random

red = ["0","1","2","3","4","5","6","7","8","9","stop","reverse","draw2"]
orange = ["0","1","2","3","4","5","6","7","8","9","stop","reverse","draw2"]
green = ["0","1","2","3","4","5","6","7","8","9","stop","reverse","draw2"]
blue = ["0","1","2","3","4","5","6","7","8","9","stop","reverse","draw2"]
black = ["cc","cc","cc","cc","draw4","draw4","draw4","draw4"]
colors = [red, orange, green, blue, black]

choose_deck = colors[random.randint(0,4)]
choose_card = choose_deck[random.randint(0, len(choose_deck)-1)]
print("Your card is: " + choose_card + " from the deck: " + str(choose_deck))
import random

class draw_card:
    deck = ["red_0",    "red_1",    "red_2",    "red_3",    "red_4",        "red_5",        "red_6",        "red_7",        "red_8",    "red_9",    "red_10",     "red_11",      "red_12",
        "orange_0",  "orange_1", "orange_2", "orange_3", "orange_4",     "orange_5",     "orange_6",     "orange_7",     "orange_8", "orange_9", "orange_10",  "orange_11",   "orange_12",
        "green_0",   "green_1",  "green_2",  "green_3",  "green_4",      "green_5",      "green_6",      "green_7",      "green_8",  "green_9",  "green_10",   "green_11",    "green_12",
        "blue_0",    "blue_1",   "blue_2",   "blue_3",   "blue_4",       "blue_5",       "blue_6",       "blue_7",       "blue_8",   "blue_9",   "blue_10",    "blue_11",     "blue_12",
        "black_13",  "black_13", "black_13", "black_13", "black_14",  "black_14",  "black_14",  "black_14"]

    card = deck[random.randint(0, len(deck)-1)]
    print(card)

    color, value = card.split("_")
    value = int(value)
    print(color)
    print(value)

    action = ""
    if value == 10:
        action = "stop"
        #proceed with the stop action
        print("Your card's colors is: " + color + " and it's a " + action + " card.")
    elif value == 11:
        action = "reverse"
        print("Your card's colors is: " + color + " and it's a " + action + " card.")
    elif value == 12:
        action = "draw 2"
        print("Your card's colors is: " + color + " and it's a " + action + " card.")
    elif value == 13:
        action = "chance color"
        print("Your card's colors is: " + color + " and it's a " + action + " card.")
    elif value == 14:
        action = "draw 4"
        print("Your card's colors is: " + color + " and it's a " + action + " card.")
    else:
        print("Your card's colors is: " + color + " and it's number is " + str(value) + " card.")
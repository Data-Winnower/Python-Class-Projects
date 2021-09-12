# Kale Perry
# Programming Concepts and Applications
# CSC1570-4914 Fall 2020
# 28 October 2020
# Uno Card Game

# This program will simulate the popular card game Uno (7)

import random

# the deck will be a 2-dim list
# Start with a blank list of 108 blank lists
one_deck = [["",""]]*108

# Create blank lists for all hands
player1_hand = []
player2_hand = []
player3_hand = []
computer_hand = []

# Create Constants for the values of special cards
SPECIAL_VALUE = 10
WILD_VALUE = 15
DRAW4_VALUE = 20
# Set game perimeters
CARDS_PER_PLAYER = 7


# Function - Main
def main():
        
        # Opening anoucement
        announce()

        # Build the full deck
        build_deck()

        #Deal Cards
        deal_cards()
    
        # Determine who has the best hand
        # And announce the winner(s)
        winning_hand()
    
    
# Function - opening announcement
def announce():
    print ("Welcome to 'ONE!'")
    print ("The computer game that was")
    print ("ABSOLUTELY NOT")
    print ("stolen from the card game Uno")
    print ("")
    
# Function - Build the deck
def build_deck():
    global one_deck
       
    #Add the color cards
    CARD_COLORS = ["RED", "YELLOW", "BLUE", "GREEN"] 
    CARD_VALUES = ["0","1","1","2","2","3","3","4","4",
               "5","5","6","6","7","7","8","8","9",
               "9","Skip","Skip","Reverse","Reverse",
               "Draw 2", "Draw 2"] 

    index = 0
    for color in range(len(CARD_COLORS)):
        for value in range(len(CARD_VALUES)):
            one_deck[index] = [CARD_COLORS[color],CARD_VALUES[value]]
            index = index + 1
    # Add 4 of each wild card to the deck (list)
    for index in range (100, 104):
        one_deck[index] = ["Black", "Draw 4"]
    for index in range (104,108):
        one_deck [index] = ["Black", "Wild"]
  
    
# Function - Deal the cards
# Each Player (including the Computer) gets 7 cards
def deal_cards():
    
    #Deal to Computer
    deal_to_computer()

    #Deal to Player 1
    deal_to_player1()

    #Deal to Player 2 if needed
    deal_to_player2()

    #Deal to Player 3 if needed
    deal_to_player3()

       
        
# Function - Deal cards to the computer
def deal_to_computer():
    global computer_hand
    for i in range(0,CARDS_PER_PLAYER):
        card_index = random.randint(1,(len (one_deck) - 1))
        computer_hand.append(one_deck[card_index])
        del one_deck[card_index]

# Function - Deal cards to the Player 1
def deal_to_player1():
    global player1_hand
    for i in range(0,CARDS_PER_PLAYER):
        card_index = random.randint(1,(len (one_deck) - 1))
        player1_hand.append(one_deck[card_index])
        del one_deck[card_index]

# Function - Deal cards to the Player 2
def deal_to_player2():
    global player2_hand
    for i in range(0,CARDS_PER_PLAYER):
        card_index = random.randint(1,(len (one_deck) - 1))
        player2_hand.append(one_deck[card_index])
        del one_deck[card_index]

# Function - Deal cards to the Player 3
def deal_to_player3():
    global player3_hand
    for i in range(0,CARDS_PER_PLAYER):
        card_index = random.randint(1,(len (one_deck) - 1))
        player3_hand.append(one_deck[card_index])
        del one_deck[card_index]       


# Function - determine the winning hand
def winning_hand():

    #Total Points for Computer
    computer_points = points_computer()
    
    #Total Points for Player 1
    player1_points = points_player1()
    
    #Total Points for Player 2
    player2_points = points_player2()

    #Total Points for Player 3
    player3_points = points_player3()

    # Compare points to determine the winner
    top_point_getter(computer_points, player1_points, player2_points, player3_points)



# Function - calc points for Player 1
def points_player1():
    # Initialize the acculmulator
    player1_points = 0

    # To look at each of the cards in the hand
    for card in range (0,CARDS_PER_PLAYER):
        # to look at only the value (ignoring the color)
        card_value = player1_hand [card][1]
        
        # establish the point value of each card
        # number cards are worth the number in points
        # special cards reference established constants
        if card_value == "Reverse" or card_value == "Skip" or card_value == "Draw 2":
            pt_value = int(SPECIAL_VALUE)
        elif card_value == "Wild":
            pt_value = int(WILD_VALUE)
        elif card_value == "Draw 4":
            pt_value = int(DRAW4_VALUE)
        else:
            pt_value = int(card_value)
       
        # Accumulate and return the total value          
        player1_points = player1_points + pt_value

    return player1_points
       
# Function - calc points for Player 2
def points_player2():
    # Initialize the acculmulator
    player2_points = 0

    # To look at each of the cards in the hand
    for card in range (0,CARDS_PER_PLAYER):
        # to look at only the value (ignoring the color)
        card_value = player2_hand [card][1]
        
        # establish the point value of each card
        # number cards are worth the number in points
        # special cards reference established constants
        if card_value == "Reverse" or card_value == "Skip" or card_value == "Draw 2":
            pt_value = int(SPECIAL_VALUE)
        elif card_value == "Wild":
            pt_value = int(WILD_VALUE)
        elif card_value == "Draw 4":
            pt_value = int(DRAW4_VALUE)
        else:
            pt_value = int(card_value)
       
        # Accumulate and return the total value          
        player2_points = player2_points + pt_value

    return player2_points

# Function - calc points for Player 3
def points_player3():
    # Initialize the acculmulator
    player3_points = 0

    # To look at each of the cards in the hand
    for card in range (0,CARDS_PER_PLAYER):
        # to look at only the value (ignoring the color)
        card_value = player3_hand [card][1]
        
        # establish the point value of each card
        # number cards are worth the number in points
        # special cards reference established constants
        if card_value == "Reverse" or card_value == "Skip" or card_value == "Draw 2":
            pt_value = int(SPECIAL_VALUE)
        elif card_value == "Wild":
            pt_value = int(WILD_VALUE)
        elif card_value == "Draw 4":
            pt_value = int(DRAW4_VALUE)
        else:
            pt_value = int(card_value)
       
        # Accumulate and return the total value          
        player3_points = player3_points + pt_value

    return player3_points

# Function - calc points for Computer
def points_computer():
    # Initialize the acculmulator
    computer_points = 0

    # To look at each of the cards in the hand
    for card in range (0,CARDS_PER_PLAYER):
        # to look at only the value (ignoring the color)
        card_value = computer_hand [card][1]
        
        # establish the point value of each card
        # number cards are worth the number in points
        # special cards reference established constants
        if card_value == "Reverse" or card_value == "Skip" or card_value == "Draw 2":
            pt_value = int(SPECIAL_VALUE)
        elif card_value == "Wild":
            pt_value = int(WILD_VALUE)
        elif card_value == "Draw 4":
            pt_value = int(DRAW4_VALUE)
        else:
            pt_value = int(card_value)
       
        # Accumulate and return the total value          
        computer_points = computer_points + pt_value

    return computer_points

# Function - determine winner and print to screen
def top_point_getter(computer_points, player1_points, player2_points, player3_points):
    print ("Player 1 holds:")
    print (player1_hand)
    print ("Player 1 has", player1_points, "points")
    print ("")
    
    print ("Player 2 holds")
    print (player2_hand)
    print ("Player 2 has", player2_points, "points")
    print ("")
    
    print ("Player 3 holds")
    print (player3_hand)
    print ("Player 3 has", player3_points, "points")
    print ("")
    
    print ("Computer holds")
    print (computer_hand)
    print ("Computer has", computer_points, "points")
    print ("")
    
    #create a new list with all the total scores
    everyones_total_pts = [computer_points, player1_points, player2_points, player3_points]

    # find the high score
    high_score = max (everyones_total_pts)
    print ("With a total score of", high_score)
    if high_score == player1_points:
        print ("Player 1 Wins!")
    if high_score == player2_points:
        print ("Player 2 Wins!")             
    if high_score == player3_points:
        print ("Player 3 Wins!")
    if high_score == computer_points:
        print ("Computer Wins!")
                   

# Call the Main Function
main()

# Included only for proving that cards held
# by players are no longer in the deck
print ("")
print ("")
print ("Just to verify,")
print ("Cards still in the deck:")
print (one_deck)

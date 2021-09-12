####MR. BRYSON####
# Please note: there is a lot of output
# print to the screen during the course of play
# that is so you can clearly see what is happening
# I would structure the output differently
# if the goal was to actually have someone
# play this (which would be lame)
# rather than grade this.
# You're welcome.

# Kale Perry
# Programming Concepts and Applications
# CSC1570-4914 Fall 2020
# 25 November 2020
# Statego

# This program will use the game peices
# of Statego to simulate game play
# similar to the card game "War"

# Game parameters employed in this program:
# Each battle is one randomly selected
# game peice from each team going head-to-head
# winner of the round is based on Stageto rank
# and special properties (i.e. miners can defuse bombs etc)
# Winner of the round goes on to the next round
# vs a new random draw from opponeant.
# Loser of the round is not reusable (they are dead)
# Exception: bombs are not reusable even when they win.
# After a bomb is used, that team will
# use a new random selection in the next battle.
# Game ends when one team's flag is captured
# a.k.a. when either team's flag goes into battle.
# If both flags go into battle against each other
# the game is a draw.
# Otherwise, the flag is captured in the battle
# and the team sending their flag into battle loses.

import random
     
# Create a class for a team
# each player will start with a full team
class Team:
    def __init__(self):
        self.team = []

    # Some pieces appear in multiples on a team
    # thus the itterations when adding them
    def set_team(self):
        for i in range (0,6):
            self.team.append ("Bomb") # 6 bombs per team
        self.team.append ("Marshal") # 1 marshal per team
        self.team.append ("General") # 1 general per team
        for i in range (0,2):
            self.team.append ("Colonel")# 2 colonels per team
        for i in range (0,3):
            self.team.append ("Major") # 3 majors per team
        for i in range (0,4):
            self.team.append ("Captain") # 4 captains per team
        for i in range (0,4):
            self.team.append ("Lieutenant") # 4 lieutenants per team
        for i in range (0,4):
            self.team.append ("Sergeant") # 4 sergeants per team
        for i in range (0,5):
            self.team.append ("Miner") # 5 miners per team
        for i in range (0,8):
            self.team.append ("Scout") # 8 scouts per team
        self.team.append ("Spy") # 1 spy per team
        self.team.append ("Flag") # 1 flag per team
                  
        return self.team
               
# Create a class for an individual
# game piece, randomly selected 
# from a team.
# This class is NOT structured as a child class
class Game_Piece:
    def __init__(self,team):
        self.team = team
        
    # Select a random piece from each team   
    def set_index(self,team):
        index = random.randint(0,(len(team)-1))
       
        return index
       
    
###########################################################################
# Function Main
def main():

    # Opening announcement
    announce()

    # Players select their color
    color1 = select_color1()
    color2 = select_color2()
    print("")

    # Setup the two teams
    team1, team2 = create_team()
    

    # Generate first random selection
    # from team 1
    team1,piece_team1 = select_piece_team1(team1,color1)

    # Generate first random selection
    # from team 2
    team2,piece_team2 = select_piece_team2(team2,color2)

    # Game Play determines the winner of each battle
    # and when the game is over
    game_over = 0
    while game_over == 0:
        game_over = game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)

    
# End of Main
###########################################################################
# Begin prelim functions

# Function - Opening Announcement
def announce():
    print ("Let's simulate the game of Stratego")
    print ("Two players will each select a team color.")
    print ("Then randomly selected pieces will battle")
    print ("head-to-head, until one team ")
    print ("captures the other team's flag.")
    start = input ("Hit enter when you are ready to begin.")
    print ("")
           
# Functions - Each player selects their color
# In retrospect,
# I probably could create a color class
# and set_color and get_color methods
# and then 2 instances of that class
# BUT, the code I have written works
# and I don't want to screw with it.
def select_color1():
    color1 = input("Player 1, please enter any color: ")
    return color1

def select_color2():
    color2 = input("Player 2, please enter any color: ")
    return color2

# Function - create two instances of Team
def create_team():
    team1 = Team()
    team1 = team1.set_team()
    
    team2 = Team()
    team2 = team2.set_team()
    
    return team1,team2

# End prelim functions
###########################################################################

# Function - Game Play
# Determines the winner in each battle
# Determines if game is over (flag is captured)
def game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2):    

    # Determine the winner of each 'battle'
    # Based on 6 general cases
    # and 3 sub-cases under the first general case

    # Case One - same peices for each team = draw
    if piece_team1 == piece_team2:
        
        
        # Special Case flag vs flag
        if piece_team1 == "Flag":
            print (" Flag vs. Flag")
            print ("")
            game_over = 3
            # Announce the winner of the game
            announce_winner(game_over,color1,color2,team1,team2)

        # Special Case bomb vs bomb
        elif piece_team1 == "Bomb":
            print ("Bomb vs Bomb")
            print ("Mutual distruction")
            go = input ("Press enter to start the next battle")
            print ("")
            team1,piece_team1 = select_piece_team1(team1,color1)
            team2,piece_team2 = select_piece_team2(team2,color2)
            game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)

        # Special Case equal pieces, not flag or bomb
        else:
            print (color1,piece_team1,"vs.", color2,piece_team2)
            print ("The battle is a draw: both die")
            go = input ("Press enter to start the next battle")
            print ("")
           
            # Select the next piece for each team for next battle
            team1,piece_team1 = select_piece_team1(team1,color1)
            team2,piece_team2 = select_piece_team2(team2,color2)
            game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)
            
    # Case Two - Flag is captured
    elif piece_team1 == "Flag":
            game_over = 2
            # Announce the winner of the game
            announce_winner(game_over,color1,color2,team1,team2)
    elif piece_team2 == "Flag":
            game_over = 1
            # Announce the winner of the game
            announce_winner(game_over,color1,color2,team1,team2)

    # Case Three - one bomb (not vs miner)
    # Bombs are not reusable
    elif piece_team1 == "Bomb" and piece_team2 != "Miner":
        print (color1,piece_team1,"vs.", color2,piece_team2)
        print (color1,piece_team1,"blows up",color2,piece_team2)
        go = input ("Press enter to start the next battle")
        print ("")
        # Select the next piece for each team for next battle
        team1,piece_team1 = select_piece_team1(team1,color1)
        team2,piece_team2 = select_piece_team2(team2,color2)
        game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)
    elif piece_team2 == "Bomb" and piece_team1 != "Miner":
        print(color1,piece_team1,"vs.", color2,piece_team2)
        print (color2,piece_team2,"blows up",color1,piece_team1)
        go = input ("Press enter to start the next battle")
        print ("")
        # Select the next piece for each team for next battle
        team1,piece_team1 = select_piece_team1(team1,color1)
        team2,piece_team2 = select_piece_team2(team2,color2)
        game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)
        
    # Case Four Bomb vs Miner
    # Bombs are not reusable
    elif piece_team1 == "Bomb" and piece_team2 == "Miner":
        print(color1,piece_team1,"vs.", color2,piece_team2)
        print (color2, piece_team2,"defuses",color1,piece_team1)
        go = input ("Press enter to start the next battle")
        print ("")
        # Select the next piece for each team for next battle
        team1,piece_team1 = select_piece_team1(team1,color1)
        game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)
    elif piece_team2 == "Bomb" and piece_team1 == "Miner":
        print(color1,piece_team1,"vs.", color2,piece_team2)
        print (color1, piece_team1,"defuses",color2,piece_team2)
        go = input ("Press enter to start the next battle")
        print ("")
        # Select the next piece for each team for next battle
        team2,piece_team2 = select_piece_team2(team2,color2)
        game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)
    
    # Case Five - Team 1 wins battle
    # Team 1 piece will continue to next battle
    elif ((piece_team1 == "Spy" and(piece_team2 == "Marshal" or
        piece_team2 == "General")) or(piece_team1 == "Scout" and
        piece_team2 == "Spy")or(piece_team1 == "Miner" and
        (piece_team2 == "Scout" or piece_team2 == "Spy")) or
        (piece_team1 == "Sergeant" and
        (piece_team2 == "Miner" or piece_team2 == "Scout" or
        piece_team2 == "Spy")) or(piece_team1 == "Lieutenant" and
        (piece_team2 == "Sergeant" or piece_team2 == "Miner" or
        piece_team2 == "Scout" or piece_team2 == "Spy")) or
        (piece_team1 == "Captain" and (piece_team2 == "Lieutenant" or
        piece_team2 == "Sergeant" or piece_team2 == "Miner" or
        piece_team2 == "Scout" or piece_team2 == "Spy")) or
        (piece_team1 == "Major" and (piece_team2 == "Captain" or
        piece_team2 == "Lieutenant" or piece_team2 == "Sergeant" or
        piece_team2 == "Miner" or piece_team2 == "Scout" or
        piece_team2 == "Spy")) or(piece_team1 == "Colonel" and
        (piece_team2 == "Major" or piece_team2 == "Captain" or
        piece_team2 == "Lieutenant" or piece_team2 == "Sergeant" or
        piece_team2 == "Miner" or piece_team2 == "Scout" or
        piece_team2 == "Spy")) or(piece_team1 == "General" and
        (piece_team2 == "Colonel" or piece_team2 == "Major" or
        piece_team2 == "Captain" or piece_team2 == "Lieutenant" or
        piece_team2 == "Sergeant" or piece_team2 == "Miner" or
        piece_team2 == "Scout")) or
        (piece_team1 == "Marshal" and (piece_team2 == "General" or
        piece_team2 == "Colonel" or piece_team2 == "Major" or
        piece_team2 == "Captain" or piece_team2 == "Lieutenant" or
        piece_team2 == "Sergeant" or piece_team2 == "Miner" or
        piece_team2 == "Scout"))):
  
        print(color1,piece_team1,"vs.", color2,piece_team2) 
        print (color1,piece_team1,"wins this battle")
        go = input ("Press enter to start the next battle")
        print ("")
        # Select a new piece for team 2 for next battle
        team2,piece_team2 = select_piece_team2(team2,color2)
        game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)

    # Case Six - Team 2 wins battle
    # Team 2 piece will continue to next battle
    else:
        print(color1,piece_team1,"vs.", color2,piece_team2)
        print (color2,piece_team2,"wins this battle")
        go = input ("Press enter to start the next battle")
        print ("")
        #select a new piece for team 1 for the next battle
        team1,piece_team1 = select_piece_team1(team1,color1)
        game_play(game_over,piece_team1,team1,color1,piece_team2,team2,color2)
###########################################################################
        
            
# Function - Generate a random selection
# from remaining pieces on team 1
def select_piece_team1(team1,color1):
    piece_team1 = Game_Piece(team1)
    index_team1 = piece_team1.set_index(team1)
    piece_team1 = team1[index_team1]
    print ("The",color1, "team selects a", piece_team1)
    del team1[index_team1]
    return team1,piece_team1
                   
# Function - Generate a random selection
# from remaining pieces on team 2
def select_piece_team2(team2,color2):
    piece_team2 = Game_Piece(team2)
    index_team2 = piece_team2.set_index(team2)
    piece_team2 = team2[index_team2]
    print ("The",color2, "team selects a", piece_team2)
    del team2[index_team2]
    return team2,piece_team2

# Function - Game is Over
# Announce the results/winner
def announce_winner(game_over,color1,color2,team1,team2):
    
    if game_over == 3:
        print ("The game has ended in a draw")
    elif game_over == 2:
        print (color2, "has captured the", color1, "Flag.")
        print (color2, "WINS")
    elif game_over == 1:
        print (color1, "has captured the", color2, "Flag.")
        print (color1, "WINS")
    else:
        print ("Something has gone wrong.")
        print ("Looks like armagedon")

    # The following is included solely 
    # for the purposes of verifying
    # that pieces are removed from play
    # after they have been used in battle
    print ("")
    print ("For verification.....")
    print (color1,"Team has the following pieces remaining:")
    print (team1)
    print ("")
    print (color2,"Team has the following pieces remaining:")
    print (team2)
    print ("")
    print ("Note: Remaining piece count on each team may not be the")
    print ("same since battle winners go on to the next battle")
    print ("")
    print ("THANKS MR BRYSON")
    print ("for a great semester and lots of learning!")
    print ("I'll keep in touch.")
           

# Call the Main
main()















    

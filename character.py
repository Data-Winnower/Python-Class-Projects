# Kale Perry
# Programming Concepts and Applications
# CSC1570-4914 Fall 2020
# 13 November 2020
# Character/Player

# This program will create characters and their attributes
# the idea being that these characters are then used
# in some sort of game play in other programs

import random

# Character class
# Creates a class for characters to be used for game play
class Character:
    def __init__(self):
        self.__name = 0
        self.__sex = 0
        self.__gender = 0
        self.__orientation = 0
        self.__weapon = 0
        self.__outfit = 0

    # Set Name method generates a random
    # name for a character
    def set_name(self):
        self.__name = random.randint(1,10)
        if self.__name == 1:
            self.__name = "Pat"
        elif self.__name == 2:
            self.__name = "Taylor"
        elif self.__name == 3:
            self.__name = "Alex"
        elif self.__name == 4:
            self.__name = "Skyler"
        elif self.__name == 5:
            self.__name = "Carmen"
        elif self.__name == 6:
            self.__name = "Corey"
        elif self.__name == 7:
            self.__name = "Emery"
        elif self.__name == 8:
            self.__name = "Jordan"
        elif self.__name == 9:
            self.__name = "Kelly"
        else:
            self.__name = "Bailey"
        return self.__name
    
    # Set Sex method generates a random
    # biological sex for a character
    def set_sex(self):
        self.__sex = random.randint(1,5)
        if self.__sex == 1:
            self.__sex = "male"
        elif self.__sex == 2:
            self.__sex = "female"
        elif self.__sex == 3:
            self.__sex = "chimera"
        elif self.__sex == 4:
            self.__sex = "mosaic"
        else:
            self.__sex = "intersex person"
        return self.__sex
    
    # Set Gender method generates a random
    # gender for a character
    def set_gender(self):
        self.__gender = random.randint(1,11)
        if self.__gender == 1:
            self.__gender = "agender"
        elif self.__gender == 2:
            self.__gender = "aporagender"
        elif self.__gender == 3:
            self.__gender = "bigender"
        elif self.__gender == 4:
            self.__gender = "gender fluid"
        elif self.__gender == 5:
            self.__gender = "intergender"
        elif self.__gender == 6:
            self.__gender = "neutrios"
        elif self.__gender == 7:
            self.__gender = "nonbinary"
        elif self.__gender == 8:
            self.__gender = "omnigender"
        elif self.__gender == 9:
            self.__gender = "man"
        elif self.__gender == 10:
            self.__gender = "woman"
        else:
            self.__gender = "two-spirit"
        return self.__gender
    
    # Set Orientation method generates a random
    # orientation for a character
    def set_orientation(self):
        self.__orientation = random.randint(1,6)
        if self.__orientation == 1:
            self.__orientation = "asexual"
        elif self.__orientation == 2:
            self.__orientation = "androsexual"
        elif self.__orientation == 3:
            self.__orientation = "autosexual"
        elif self.__orientation == 4:
            self.__orientation = "gynosexual"
        elif self.__orientation == 5:
            self.__orientation = "omnisexual"
        else:
            self.__orientation = "androsexual"
        return self.__orientation

    # Set Weapon method generates a random
    # weapon for a character
    def set_weapon(self):
        self.__weapon = random.randint(1,9)
        if self.__weapon == 1:
            self.__weapon = "sarcasm"
        elif self.__weapon == 2:
            self.__weapon = "dark humor"
        elif self.__weapon == 3:
            self.__weapon = "animal magnetism"
        elif self.__weapon == 4:
            self.__weapon = "intellegence"
        elif self.__weapon == 5:
            self.__weapon = "courage"
        elif self.__weapon == 6:
            self.__weapon = "self confidence"
        elif self.__weapon == 7:
            self.__weapon = "honesty"
        elif self.__weapon == 8:
            self.__weapon = "wit"
        else:
            self.__weapon = "spirituality"
        return self.__weapon

    def set_outfit(self):
        char_outfit = Outfit()
        shoes = char_outfit.set_shoes()
        bottom = char_outfit.set_bottom()
        top = char_outfit.set_top()
        hat = char_outfit.set_hat()
        return shoes,bottom,top,hat

    def get_char(self):
        return self.__name,self.__sex,self.__gender,self.__orientation,self.__weapon,shoes,bottom,top,hat

class Outfit:
    def __init__ (self):
        self.__shoes = 0
        self.__bottom = 0
        self.__top = 0
        self.__hat = 0
        
    
    # Set Shoes method generates a random
    # shoe type for the oputfit
    def set_shoes(self):
        self.__shoes = random.randint(1,7)
        if self.__shoes == 1:
            self.__shoes = "flip-flops"
        elif self.__shoes == 2:
            self.__shoes = "combat boots"
        elif self.__shoes == 3:
            self.__shoes = "Air Jordans"
        elif self.__shoes == 4:
            self.__shoes = "Berkinstocks"
        elif self.__shoes == 5:
            self.__shoes = "stilettos"
        elif self.__shoes == 6:
            self.__shoes = "cowboy boots" 
        else:
            self.__shoes = "Walmart special sneakers"
        return self.__shoes
    
    def set_bottom(self):
        self.__bottom = random.randint(1,6)
        if self.__bottom == 1:
            self.__bottom = "rainbow-colored kilt"
        elif self.__bottom == 2:
            self.__bottom = "saggy skinny jeans"
        elif self.__bottom == 3:
            self.__bottom = "fancy purple pants"
        elif self.__bottom == 4:
            self.__bottom = "tan khakis"
        elif self.__bottom == 5:
            self.__bottom = "black cargo shorts"
        else:
            self.__bottom = "grey sweatpants"
        return self.__bottom
    
    def set_top(self):
        self.__top= random.randint(1,6)
        if self.__top == 1:
            self.__top = "dirty wife-beater"
        elif self.__top == 2:
            self.__top = "t-shirt that reads 'Best Dad Ever'"
        elif self.__top == 3:
            self.__top = "black hoody"
        elif self.__top == 4:
            self.__top = "pink lace bra"
        elif self.__top == 5:
            self.__top = "red, white, & blue golf shirt"
        else:
            self.__top = "topless upper half" 
        return self.__top
    
    def set_hat(self):
        self.__hat= random.randint(1,6)
        if self.__hat == 1:
            self.__hat = "a grey fedora with a feather"
        elif self.__hat == 2:
            self.__hat = "a red MAGA cap"
        elif self.__hat == 3:
            self.__hat = "a green beanie"
        elif self.__hat == 4:
            self.__hat = "a fur-lined trapper hat"
        elif self.__hat == 5:
            self.__hat = "a brown bowler"
        else:
            self.__hat = "one of those ten-gallon hats like John Wayne used to wear" 
        return self.__hat
    
    def get_outfit(self):
        return self.__shoes, self.__bottom, self.__top, self.__hat

# Function Main
def main():

    # Opening announcement
    announce()

    # Go again?
    again = go_again()


    # If user wants to continue
    while again == "Y" or again == "y":
        # Create a character
        your_character = Character()
        your_character.get_char
        output_character(your_character)
        # Go again?
        again = go_again()
    # If user chooses to quit
    else:
        print ("GOODBYE")

# Function - Announcement
def announce():
    print ("Welcome to Character Central")
    print ("We will randomly generate a character")
    print ("for you to use in game play.")
    print ("")

# Function - Go Again?
def go_again():
        again = input("Would you like me to generate a new character for you now? Y/N: ")
        return again

# Function - Output the Character's characteristics
def output_character(your_character):
    name = your_character.set_name()
    weapon = your_character.set_weapon()
    orientation = your_character.set_orientation()
    gender = your_character.set_gender()
    sex = your_character.set_sex()
    shoes,bottom,top,hat = your_character.set_outfit()
    print ("-------------------------------------------------")
    print ("Your character's name is", name)
    print ("")
    print ("You will recognise",name)
    print ("by their", bottom,"and",top,)
    print ("worn with",shoes,"and",hat)
    print ("")
    print (name,"'s weapon of choice is their",weapon)
    print ("")
    print ("Make sure to honor",name,"'s identity as")
    print ("a(n)", orientation, gender, sex)
    print ("-------------------------------------------------")
    
    
# Call the main
main()

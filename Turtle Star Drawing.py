# Kale Perry
# Programming Concepts and Applications
# CSC1570-4914 Fall 2020
# 01 October 2020
# Repeating Turtle
# Repeating Turtle
# Repeating Turtle
# Did I remember to say, Repeating Turtle?

import turtle
turtle.speed(5)
again = "Yes"
print ("LET'S DRAW A STAR!")
while again =="Yes" or again == "Y" or again == "yes" or again =="y":
    points = int(input("How many points would you like on your star? Pick 5 - 30: "))
    print ("")
    if points >=5 and points <= 30:
        print ("OK, a ",points,"-pointed star it is.")
    else:
        print ("What part of pick a number from 5 to 30 did you not understand?")
                  

    # Set the turning angle for each possible point count
    if points == 5:
        angle = 36
    elif points==7:
        angle = 180/7
    elif points == 8:
        angle = 45
    elif points == 9:
        angle = 20
    elif points == 10:
        angle = 72
    elif points == 11:
        angle = 180/11
    elif points == 12:
        angle = 30
    elif points ==13:
        angle = 180/13
    elif points == 14:
        angle = 540/10.5
    elif points == 15:
        angle = 12
    elif points == 16:
        angle = 22.5
    elif points == 17:
        angle=180/17
    elif points == 18:
        angle = 40
    elif points == 19:
        angle = 180/19
    elif points == 20:
        angle = 18
    elif points == 21:
        angle = 180/21
    elif points == 22:
        angle = 360/11
    elif points == 23:
        angle = 180/23
    elif points == 24:
        angle = 15
    elif points == 25:
        angle = 7.2
    elif points == 26:
        angle = 90-(180/26)
    elif points == 27:
        angle = 180/27
    elif points == 28:
        angle = 540/14
    elif points == 29:
        angle = 180/29
    elif points == 30:
        angle = 24
    # I could keep going and add as many more
    # as I feel like figuring out the angle for

    turtle.clear()
    if points >=5 and points <= 30 and points!=6:
        for x in range (points):
            turtle.pencolor("magenta")
            turtle.forward(250)
            turtle.left(angle+180)

    elif points == 6:
        for x in range (6):
            turtle.pencolor("blue")
            turtle.forward(80)
            turtle.right (60)
            turtle.forward (80)
            turtle.left(120)

    again = input("Would you like to draw another?")

    
# Don't judge me - this was fun for me!
# Figuring out the angles was quite the challenge.
# And yeah, I cheated a little by not making all of them
# really pointy -
# compare 25 points to 26 points.
# Once I got it to work -
# Pointy or not, I called it good!
# And I had to go a whole other route
# to make a 6 pointed star.
# But, hey.....geometry wasn't the point
# of the assignment.


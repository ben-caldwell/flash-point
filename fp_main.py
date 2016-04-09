import pygame, sys, random
from pygame.locals import *
from fp_variables import *
from fp_classes import *

#Initialises the pygame module
pygame.init()

def main():
    #Iterate through each value of the 2D list, square, and add an object to that coordinate
    for col in square:
        for y in col:
            x = square.index(col)
            w = layout[y][x]
            Square(x, y, w)
    #Setting the spawn square at coordinates (2,3) and setting the dimensions of the player rectabgle
    start_square = square[2][3]
    player = Player(start_square, Rect(start_square.x-5, start_square.y-5, 10, 10))

    while True:
        #After each loop fill screen with blank color and redraw each object
        screen.fill(bg_color)
        for event in pygame.event.get():
            #When the user exits the game quit the pygame module
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                player.move(event)
            #When the user clicks the left mouse button (1) check each of the doors on the players square and open/close
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in player.square.door_objects:
                        player.square.door_objects[i].action_door(event)
        for i in list_of_objects:
            i.draw_self()
            
        pygame.display.update()
        clock.tick(fps)

main()

#Below loop can be used for debugging as it restarts instead of crashing

##while True:
##    try:
##        main()
##    except:
##        continue

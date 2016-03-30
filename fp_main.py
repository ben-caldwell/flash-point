import pygame, sys, random
from pygame.locals import *
from fp_variables import *
#from fp_functions import *
from fp_classes import *

pygame.init()

def main():
    
    #Initialise the board assign instances of the object Square to the 2d list holding the board and then give it walls according to the letter
    for x in range(number_cols):
        for y in range(number_rows):
            i = Square(x, y)
            w = layout[y][x]
            
            if layout[y][x] == 'r' or layout[y][x] == '-':
                i.walls[0][0] = True
            if layout[y][x] == 'r' or layout[y][x] == 'l':
                i.walls[3][0] = True
    #"spawn" the player
    square[3][3].player = True 
    
    #The game loop, while this is running the game is open
    while True:
        screen.fill(bg_color)
        #Everytime an event happens check what it is and carry out actions accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                #iterate through square and move the player
                for col in square:
                    for obj in col:
                        obj.move_player(event)
        
        #iterate through square to draw the walls each frame
        for col in square:
            for obj in col:
                obj.draw_self()

        pygame.display.update()
        clock.tick(fps)

main()

#You can use the below loop to test the code ignoring any errors, restarting if an error is thrown
##while True:
##    try:
##        main()
##    except:
##        continue

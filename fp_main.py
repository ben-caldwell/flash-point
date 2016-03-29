import pygame, sys, random
from pygame.locals import *
from fp_variables import *
#from fp_functions import *
from fp_classes import *

pygame.init()

def main():

    for x in range(number_cols):
        for y in range(number_rows):
            i = Square(x, y)
            w = layout[y][x]
            
            if layout[y][x] == 'r' or layout[y][x] == '-':
                i.walls[0][0] = True
            if layout[y][x] == 'r' or layout[y][x] == 'l':
                i.walls[3][0] = True

    square[3][3].player = True 

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                for col in square:
                    for obj in col:
                        obj.move_player(event)

        for col in square:
            for obj in col:
                obj.draw_self()

        pygame.display.update()
        clock.tick(fps)

main()

##while True:
##    try:
##        main()
##    except:
##        continue

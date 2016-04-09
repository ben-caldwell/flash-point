import pygame, sys, random
from pygame.locals import *
from fp_variables import *
from fp_classes import *

pygame.init()

def main():

    for col in square:
        for y in col:
            x = square.index(col)
            w = layout[y][x]
            Square(x, y, w)

    start_square = square[2][3]
    player = Player(start_square, Rect(start_square.x-5, start_square.y-5, 10, 10))

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                player.move(event)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in player.square.door_objects:
                        player.square.door_objects[i].action_door(event)
        for i in list_of_objects:
            i.draw_self()
            
        pygame.display.update()
        clock.tick(fps)

main()

##while True:
##    try:
##        main()
##    except:
##        continue

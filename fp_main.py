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
            i = Square(x, y, w)
                
    square[0][0].player = True 

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                for col in square:
                    for obj in col:
                        check_move = obj.move_player(event)
                        if check_move:
                            break
                    if check_move:
                        break

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

import pygame, sys, random
from pygame.locals import *

#Initialising colours in a dictionary for easier reference
c = {
    'wh': (255, 255, 255),
    'bl': (  0,   0,   0),
    'bu': (  0,   0, 255),
    're': (255,   0,   0),
    'gr': (  0, 155,   0),
    'ma': (128,   0,   0),
    'na': (  0,   0, 128),
    'pu': (128,   0, 128),
    'si': (192, 192, 192),
    'dg': (100, 100, 100)
}

bg_color = c['si']

#Sets the layout of the room, the Square object reads its letter and gives itself values accordingly
"""
walls:
    - = top
    l = left
    r = corner

doors:
    r:
      T = door on top of corner
      s = door on left of corner

    _ = door on top
    L = door on left
    
"""
layout = [
    "          ",
    " r--s-T--l",
    " l  l L  l",
    " L s---r_l",
    " l l   L L",
    " r--_-r-rl",
    " l    L Ll",
    " --_----- "
]

#The values the letter provides
"""
'x':[top wall, left wall, top door, left door]
"""

layout_ref = {
    'r':[True, True, False, False],
    's':[True, True, False, True],
    'T':[True, True, True, False],
    '-':[True, False, False, False],
    '_':[True, False, True, False],
    'l':[False, True, False, False],
    'L':[False, True, False, True],
    ' ':[False, False, False, False],
    #'.':[False, False, False, False] - unused, was going to be small dot to complete corner
}



#Initialises controls, the arrow keys can be uncommented to use those instead of wasd

##key_up = pygame.K_UP
##key_down = pygame.K_DOWN
##key_left = pygame.K_LEFT
##key_right = pygame.K_RIGHT

key_up = pygame.K_w
key_down = pygame.K_s
key_left = pygame.K_a
key_right = pygame.K_d
key_space = pygame.K_SPACE

#Initialises lists used and sets the top_left value of the board
top_left = [100, 100]
list_of_doors = []
list_of_walls = []
list_of_objects = []

#Reads the layout list and gives numerical values to the dimensions of the board
number_rows = len(layout)
number_cols = len(layout[0])

#A list comprehension to initialise the 2D list of the board so that object Squares can be added to the coordinates
square = [[y for y in range(number_rows)] for x in range(number_cols)]

#FPS
fps = 30
clock = pygame.time.Clock()

#Initialising screen
scr_width = top_left[0]*2 + 80*(number_cols-1)
scr_height = top_left[1]*2 + 80*(number_rows-1)
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Flashpoint')


#### Empty House
##layout = [
##    "          ",
##    " r-------l",
##    " l       l",
##    " l       l",
##    " l       l",
##    " l       l",
##    " l       l",
##    " --------."
##]


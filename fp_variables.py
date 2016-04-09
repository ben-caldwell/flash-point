import pygame, sys, random
from pygame.locals import *

#Initialising colours
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

"""
doors:
    r:
      T = top on r
      s = side on r
"""
layout = [
    "          ",
    " r--s-T--l",
    " l  l L  l",
    " L s---r_l",
    " l l   L L",
    " r--_-r-rl",
    " l    L Ll",
    " --_-----."
]

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
    '.':[False, False, False, False]
}

#Initialising controls
##key_up = pygame.K_UP
##key_down = pygame.K_DOWN
##key_left = pygame.K_LEFT
##key_right = pygame.K_RIGHT

key_up = pygame.K_w
key_down = pygame.K_s
key_left = pygame.K_a
key_right = pygame.K_d
key_space = pygame.K_SPACE

#Game
top_left = [100, 100]
list_of_doors = []
list_of_walls = []
list_of_objects = []

directions = [
    'up',
    'down',
    'left',
    'right'
]


number_rows = len(layout)
number_cols = len(layout[0])

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


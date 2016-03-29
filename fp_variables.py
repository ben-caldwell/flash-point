import pygame, sys, random
from pygame.locals import *

#Initialising colours
c = {
    'wh': (255, 255, 255),
    'bl': (  0,   0,   0),
    'bu': (  0,   0, 255),
    're': (255,   0,   0),
    'gr': (  0, 255,   0),
    'ma': (128,   0,   0),
    'na': (  0,   0, 128),
    'pu': (128,   0, 128),
    'si': (192, 192, 192),
    'dg': (100, 100, 100)
}

bg_color = c['si']

#Initialising controls
key_up = pygame.K_UP
key_down = pygame.K_DOWN
key_left = pygame.K_LEFT
key_right = pygame.K_RIGHT

#Game
top_left = [100, 100]

layout = [
    "          ",
    " r--r----l",
    " l        ",
    " r- l    l",
    " l  l    l",
    " r- r- --l",
    " l       l",
    " ----- --."
]
number_rows = len(layout)
number_cols = len(layout[0])

##square = [[y for y in range(1,len(layout))] for x in range(1,len(layout[0]))]
square = [[y for y in range(number_rows)] for x in range(number_cols)]

#FPS
fps = 30
clock = pygame.time.Clock()

#Initialising screen
scr_width = top_left[0]*2 + 80*(number_cols-1)
scr_height = top_left[1]*2 + 80*(number_rows-1)
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Flashpoint')

import pygame, sys, random
from pygame.locals import *
from fp_variables import *
#from fp_functions import *

class Square(object):

    def __init__(self, x, y):
        self.fire = 'none'
        self.player = False
        self.poi = False

        self.cx = x
        self.cy = y
        
        self.length = 80
        self.x = x * self.length + top_left[0]
        self.y = y * self.length + top_left[1]

        self.walls = [
            [False, (self.x - self.length/2, self.y - self.length/2, self.length, self.length/10)],
            [False, (self.x + self.length/2, self.y - self.length/2, self.length/10, self.length)],
            [False, (self.x - self.length/2, self.y + self.length/2, self.length, self.length/10)],
            [False, (self.x - self.length/2, self.y - self.length/2, self.length/10, self.length)]
        ]

        square[x][y] = self

    def move_player(self, event):

        px = self.cx
        py = self.cy
        if self.player == True:
            if event.key == key_up and py > 0:
                py -= 1

            elif event.key == key_down and py < number_rows-1:
                py += 1

            elif event.key == key_left and px > 0:
                px -= 1

            elif event.key == key_right and px < number_cols-1:
                px += 1

            self.player = False
            square[px][py].player = True
        
    def draw_self(self):
        pygame.draw.rect(screen, c['na'], (self.x-1, self.y-1, 2, 2))
        #^^ Rectangle used to see where each square was
        if self.player:
            pygame.draw.rect(screen, c['na'], (self.x-5, self.y-5, 10, 10))
        for i in range(len(self.walls)):
            if self.walls[i][0]:
                pygame.draw.rect(screen, c['dg'], self.walls[i][1])

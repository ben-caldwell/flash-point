import pygame, sys, random
from pygame.locals import *
from fp_variables import *

class Square(object):

    def __init__(self, x, y, w):
        self.fire = 'none'
        self.player = False
        self.poi = False

        self.cx = x
        self.cy = y
        
        self.length = 80
        self.x = x * self.length + top_left[0]
        self.y = y * self.length + top_left[1]
        
        self.walls = [
            [False, False],
            [False, False],
            [False, False],
            [False, False]
        ]
        self.wall_dimensions = [
            (self.x - self.length/2, self.y - self.length/2, self.length, self.length/10),
            (self.x - self.length/2, self.y - self.length/2, self.length/10, self.length)
        ]
        self.walls[0] = layout_ref[w][0]
        self.walls[1] = layout_ref[w][1]
        self.wall_color = c['dg']

        square[x][y] = self
    
    def move_player(self, event):
        
        px = self.cx
        py = self.cy

        if self.player == True:
            if event.key == key_up and py > 0 and not self.walls[0][0]:
                py -= 1

            elif event.key == key_down and py + 1 < number_rows and not self.walls[2][0]:
                py += 1

            elif event.key == key_left and px > 0 and not self.walls[3][0]:
                px -= 1

            elif event.key == key_right and px + 1 < number_cols and not self.walls[1][0]:
                px += 1

            self.player = False
            square[px][py].player = True
            return True
        
    def draw_self(self):
        pygame.draw.rect(screen, c['na'], (self.x-1, self.y-1, 2, 2))
        #^^ Rectangle used to see where each square was
        if self.player:
            pygame.draw.rect(screen, c['na'], (self.x-5, self.y-5, 10, 10))
        
        if self.walls[0][0]:
            if self.walls[0][1]:
                self.wall_color = c['bu']
            else:
                self.wall_color = c['dg']

            pygame.draw.rect(screen, self.wall_color, self.wall_dimensions[0])

        if self.walls[1][0]:
            if self.walls[1][1]:
                self.wall_color = c['bu']
            else:
                self.wall_color = c['dg']

            pygame.draw.rect(screen, self.wall_color, self.wall_dimensions[1])

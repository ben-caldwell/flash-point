import pygame, sys, random
from pygame.locals import *
from fp_variables import *
#from fp_functions import *
#^ functions are unused at the moment

#The square object holds all the information for a tile of the board
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
        
        #The list walls, [0,1,2,3] is [top, right, bottom, left] and gives the appropriate relative position and dimensions for each direction
        self.walls = [
            [False, (self.x - self.length/2, self.y - self.length/2, self.length, self.length/10)],
            [False, (self.x + self.length/2, self.y - self.length/2, self.length/10, self.length)],
            [False, (self.x - self.length/2, self.y + self.length/2, self.length, self.length/10)],
            [False, (self.x - self.length/2, self.y - self.length/2, self.length/10, self.length)]
        ]
        
        #assign itself to the 2d array of the board so that it can be checked when iterating through square
        square[x][y] = self

    def move_player(self, event):
        
        #assign a temporary variables px and py to the players position to simplify function (could use self.cx and self.cy but I wanted to simplify for testing purposes)
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
            
            #Currently this does not work for pressing down and right (adding to px or py)
            #it instead moves the player to the end of the list, edge of the board
            #I am uncertain as to why this is a problem when subracting throws no issues so feel free to try and fix it
            
            self.player = False
            square[px][py].player = True
        
    def draw_self(self):
        pygame.draw.rect(screen, c['na'], (self.x-1, self.y-1, 2, 2))
        #^^ Rectangle used to see where each square was
        if self.player:
            pygame.draw.rect(screen, c['na'], (self.x-5, self.y-5, 10, 10))
        
        #For each direction check if a wall should be drawn
        for i in range(len(self.walls)):
            if self.walls[i][0]:
                pygame.draw.rect(screen, c['dg'], self.walls[i][1])

import pygame, sys, random
from pygame.locals import *
from fp_variables import *

class Parent(object):
    #Gives all objects with parent 'Parent' a square value which is its current square so it can be referenced
    #Sets its rectangle to be the argument rect and also adds itself to the list_of_objects so it can iterated through to, for example, draw_self
    #Also gives all the objects a method, draw_self
    def __init__(self, sq, rect):
        self.square = sq
        self.rect = rect
        list_of_objects.append(self)
        
    def draw_self(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Wall(Parent):
    #Calls parent event, sets its own variables and adds to the list_of_walls
    #List_of_walls is unused at the moment, may be removed
    def __init__(self, sq, rect):
        Parent.__init__(self, sq, rect)
        self.color = c['dg']
        list_of_walls.append(self)

class Door(Parent):
    def __init__(self, sq, rect):
        Parent.__init__(self, sq, rect)
        self.is_open = False
        self.color = c['ma']
        list_of_doors.append(self)
    
    def action_door(self, event):
        #When this method is called, in the MOUSEBUTTONDOWN event, this checks if the mouse is on top of the door and if so open/close the door and change its color accordingly
        if self.rect.collidepoint(event.pos[0], event.pos[1]):
            self.is_open = not self.is_open
            if self.is_open:
                self.color = c['gr']
            else:
                self.color = c['ma']

class Player(Parent):
    def __init__(self, sq, rect):
        Parent.__init__(self, sq, rect)
        self.color = c['na']

    def move(self, event):

        #Holds coordinate values for easier reference
        cxx = self.square.cx
        cyy = self.square.cy

        def check_collision(direction):
            #Checks if there is a wall, if so if there is a door and whether it is open or not and returns if there is a collision or not
            if self.square.check_walls[direction]:
                if self.square.check_doors[direction]:
                    if self.square.door_objects[direction].is_open:
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return False

        #Checks which key is being pressed, whether it can move there without going off the board and whether there is a collision, moves accordingly
        if event.key == key_up and cyy > 0 and not check_collision('top'):
            cyy -= 1

        elif event.key == key_down and cyy + 1 < number_rows and not check_collision('bottom'):
            cyy += 1

        elif event.key == key_left and cxx > 0 and not check_collision('left'):
            cxx -= 1

        elif event.key == key_right and cxx + 1 < number_cols and not check_collision('right'):
            cxx += 1
        else:
            return

        self.square = square[cxx][cyy]   
        self.rect = Rect(self.square.x-5, self.square.y-5, 10, 10)
            

class Square(object):
    def __init__(self, x, y, w):
        #Sets itself at the coordinate values fed in in the square 2D list and also appends itself to the list of objects
        square[x][y] = self
        list_of_objects.append(self)

        #Sets the game coordinate values, its actual (x,y) values and other variables for reference
        self.cx = x
        self.cy = y
        self.length = 80
        self.x = x * self.length + top_left[0]
        self.y = y * self.length + top_left[1]
        self.square_above = square[self.cx][self.cy-1]
        self.square_left = square[self.cx-1][self.cy]
        self.top_left_pos = [
            self.x - self.length/2 - self.length/20,
            self.y - self.length/2 - self.length/20
        ]

        #Initialises the list check_walls
        self.check_walls = {
            'top': False,
            'left': False,
            'bottom': False,
            'right': False
        }
        #Initialises the list wall_objects
        self.wall_objects = {}
        #If the layout letter indicates that there is a wall on the top of the square
        if layout_ref[w][0]:
            #Change check_walls and create an object wall at the top position
            self.check_walls['top'] = True
            self.wall_objects['top'] = Wall(self, Rect(self.top_left_pos[0], self.top_left_pos[1], self.length, self.length/10))
            if self.cy > 0:
                #If the square is not the on the top row sets the square above its variables accordingly
                self.square_above.check_walls['bottom'] = True
                self.square_above.wall_objects['bottom'] = self.wall_objects['top']
        #Same as above for left
        if layout_ref[w][1]:
            self.check_walls['left'] = True
            self.wall_objects['left'] = Wall(self, Rect(self.top_left_pos[0], self.top_left_pos[1], self.length/10, self.length))
            if self.cx > 0:
                self.square_left.check_walls['right'] = True
                self.square_left.wall_objects['right'] = self.wall_objects['left']

        #Same as above for doors
        self.check_doors = {
            'top': False,
            'left': False,
            'bottom': False,
            'right': False
        }
        self.door_objects = {}
        if layout_ref[w][2]:
            self.check_doors['top'] = True
            self.door_objects['top'] = Door(self, Rect(self.x - 10, self.y- self.length/2 - 10, 20, 20))
            if self.cy > 0:
                self.square_above.check_doors['bottom'] = True
                self.square_above.door_objects['bottom'] = self.door_objects['top']
        if layout_ref[w][3]:
            self.check_doors['left'] = True
            self.door_objects['left'] = Door(self, Rect(self.x - self.length/2 - 10, self.y - 10, 20, 20))
            if self.cx > 0:
                self.square_left.check_doors['right'] = True
                self.square_left.door_objects['right'] = self.door_objects['left']

        #Possibly thought of creating a function to shorten the above code as there are 4 similar sections but it works as is so may come back to that later
        
    def draw_self(self):
        #Draws dot to identify each square and where the board ends
        pygame.draw.rect(screen, c['na'], (self.x-1, self.y-1, 2, 2))

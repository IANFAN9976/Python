# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:40:19 2019

@author: fany
"""
#create a bear class
class bear(object):
    #initial value are the location and direction of the bear
    def __init__(self, data):
        self.row = data[0]
        self.column = data[1]
        self.direction = data[2]
    #return a string of the information of the bear
    def __str__(self):
        return 'Bear at ({},{}) moving {}'.format(self.row, self.column, self.direction)
    #define a function of move for the bear, which depends on the direction of the bear
    def move(self):
        if self.direction == 'N':
            self.row -= 1
        elif self.direction == 'S':
            self.row += 1
        elif self.direction == 'W':
            self.column -= 1
        elif self.direction == 'E':
            self.column += 1
        elif self.direction == 'NE':
            self.row -= 1
            self.column += 1
        elif self.direction == 'NW':
            self.row -= 1
            self.column -= 1
        elif self.direction == 'SE':
            self.row += 1
            self.column += 1
        elif self.direction == 'SW':
            self.row += 1
            self.column -= 1
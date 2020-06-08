# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:40:05 2019

@author: fany
"""
#create a berryfield class
class berryfield(object):
    #the initial values are the berryfield, active and reserve bears, and avtive and reserve tourists
    def __init__(self, berry):
        self.berry = berry['berry_field']
        self.ab = berry['active_bears']
        self.rb = berry['reserve_bears']
        self.at = berry['active_tourists']
        self.rt = berry['reserve_tourists']
        
    def __str__(self):
        #copy a list of the field for future use
        field = list(map(list, self.berry))
        #if there is a bear in the berryfield, there will be a B on the copy list
        for data in self.ab:
            row, col = data[0], data[1]
            if row in range(0, len(self.berry)) and col in range(0, len(self.berry)):
                field[row][col] = 'B'
        #if there is a tourist in the berryfield, there will be a T on the copy list
        for data in self.at:
            row, col = data[0], data[1]
            if row in range(0, len(self.berry)) and col in range(0, len(self.berry)):
                #if there has existed a bear, there will be an X on the copy list
                if field[row][col] == 'B':
                    field[row][col] = 'X'
                else:
                    field[row][col] = 'T'
        #return a string of the copy list
        s = ''
        for row in field:
            for value in row:
                s += '{:>4}'.format(value)
            s += '\n'
        return s
    #define a total function to print out the number of the berries in the field
    def total(self):
        t = 0
        for data in self.berry:
            t += sum(data)
        return (t, 'Field has {} berries.'.format(t))
    
    def grow(self):
        #when berry is between 1 and 9, it grows one.
        for i in range(len(self.berry)):
            for j in range(len(self.berry[i])):
                if 1 <= self.berry[i][j] < 10:
                    self.berry[i][j] += 1
        # if berry is 0 but adjacent to a 10, it grows one.
        for i in range(len(self.berry)):
            for j in range(len(self.berry)):
                if self.berry[i][j] == 0:
                    for k in range(max(0, i-1), min(len(self.berry), i+2)):
                        for l in range(max(0, j-1), min(len(self.berry), j+2)):
                            if self.berry[k][l] == 10:
                                self.berry[i][j] = 1
        
    
   

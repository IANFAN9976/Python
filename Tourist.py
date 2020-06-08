# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:40:25 2019

@author: fany
"""
#create a tourist class
class tourist(object):
    #the initial value are the location and the turns for the tourist without seeing a bear
    def __init__(self, data, turn0):
        self.row = data[0]
        self.column = data[1]
        self.turn = turn0
    #return a string of the information of the tourist
    def __str__(self):
        return 'Tourist at ({},{}), {} turns without seeing a bear.'.format(self.row, self.column, self.turn)
    
    
    
  
       
        
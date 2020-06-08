# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:18:35 2019

@author: fany
"""
#import the classes
import json
from BerryField import berryfield
from Bear import bear
from Tourist import tourist

if __name__ == "__main__":
    #input file name
    file = input('Enter the json file name for the simulation => ')
    print(file)
    print()
    #open and read file
    f = open(file)
    datas = json.loads(f.read())
    
    bfield = berryfield(datas)
    turn = 0
    total = bfield.total()
    
    #print out the information of berryfield, the active bears, and active tourists.
    print(bfield.total()[1])
    print(str(bfield))
    
    print('Active Bears:')
    for data in bfield.ab:
        print(str(bear(data)))
    print()

    print('Active Tourists:')
    for data in bfield.at:
        print(str(tourist(data,turn)))

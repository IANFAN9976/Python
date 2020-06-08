# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:33:04 2019

@author: fany
"""

import json
from BerryField import berryfield
from Bear import bear
from Tourist import tourist
if __name__ == "__main__":
    file = input('Enter the json file name for the simulation => ')
    print(file)
    print()
    f = open(file)
    datas = json.loads(f.read())
    
    bfield = berryfield(datas)
    
    print('Starting Configuration')
    print(bfield.total()[1])
    print(str(bfield))

    print('Active Bears:')
    for data in bfield.ab:
        print(str(bear(data)))
    print()

    print('Active Tourists:')
    for data in bfield.at:
        print(str(tourist(data,0)))
        
    #name the information from the class
    at = bfield.at
    #copy the active tourists for future use
    at1 = list(map(list,at))
    rt = bfield.rt
    ab = bfield.ab
    rb = bfield.rb
    bb = bfield.berry
    
    #for loop to run the first five turns
    for i in range(1,6):
        print()
        print('Turn: {}'.format(i))  
        #firstly grow the berry field
        bfield.grow()  
        #if bear does not runs into a tourist, we give him a place to calculate the berries it eats
        for b in ab:
            b_bear = bear(b)
            if len(b) == 3 and b[:2] not in at1:
                b.append(0)
            #if it has eaten berries in last turn, the berries will be back to 0
            elif len(b) == 4:
                b[3] = 0
            #if the bear is not sleeping, it eats the berries of its location
            if b[:2] not in at1 and len(b) == 4:
                b[3] += bb[b[0]][b[1]]
                bb[b[0]][b[1]] = 0
                #if the bear has not eaten 30 berries or runs into a tourist
                #it continues to move and eat
                while b[3] < 30 and b[0] in range(len(bb)) and b[1] in range(len(bb)):
                    b_bear.move()
                    b[0] = b_bear.row
                    b[1] = b_bear.column
                    #if the bear runs into a tourist, it will sleep for 3 turns
                    if b[:2] in at1:                       
                        b.append(3)
                        break
                    else:
                        if b[0] in range(len(bb)) and b[1] in range(len(bb)):
                            dif = min(bb[b[0]][b[1]], 30-b[3])
                            b[3] += dif
                            bb[b[0]][b[1]] -= dif                
            #when the bear runs into a tourist at the beginning of the turn
            #we start to count down the sleeping turn from 3
            elif len(b) == 3:
                b.append(0)
                b.append(3)
        #copy an active bear list to help remove the bears left the field from the active bear lsit    
        ab1 = ab.copy()
        for b in ab1:
            if b[0] not in range(len(bb)) or b[1] not in range(len(bb)):
                print(str(bear(b)) + ' - Left the Field')
                ab.remove(b) 
        #give the active tourists a value about the turns that not seen the bears
        for t in at:
            if len(t) == 2:
                t.append(0)
      
        for t in at:
            leave = False
            seen = 0
            #determine whether the tourist is run into by a bear
            #if so, print this tourist left the field, and remove it
            for b in ab :
                if t[:2] == b[:2] and t[:2] in at1:
                    print(str(tourist(t, t[2])) + ' - Left the Field')
                    at1.remove(t[:2])
                    leave = True
                    break
                # if a bear is inside the distance of 4, the tourist see a bear
                if (b[0]-t[0])**2 + (b[1] - t[1])**2 <= 16:
                    seen += 1
            # if a tourist sees 3 or more bears, he leaves the field       
            if seen >= 3:
                print(str(tourist(t, t[2])) + ' - Left the Field')
                at1.remove(t[:2])
                leave = True
                break
            #if the tourist leaves, skip to the next tourist
            if leave:
                continue
            #if the tourist does not see any bear, the turn gets one more
            if seen == 0:
                t[2] += 1
            #if 3 turns without see any bears, the tourist leaves
            if t[2] > 2:
                print(str(tourist(t, t[2])) + ' - Left the Field')
                at1.remove(t[:2])
        #make a new active tourist list to help get the remaining tourists
        at2 = []
        for t in at:
            if t[:2] in at1:
                at2.append(t)
        bfield.at = at2
        at = at2
        
        #print out the information of berry field
        print(bfield.total()[1])
        print(str(bfield))
    
        print('Active Bears:')
        for b in ab:
            if len(b) == 4:
                print(str(bear(b)))
            elif len(b) == 5:
                if b[4] > 1:
                    print(str(bear(b))+' - Asleep for {} more turns'.format(b[4]-1))
                else:
                    print(str(bear(b)))
                #if the bear sleep for one turn, its turns get one less
                b[4] -= 1
                if b[4] == 0:
                    b.pop()
        #print out the information of active tourists
        print()
        print('Active Tourists:')
        for t in at2:
            print(str(tourist(t, t[2])))
        print()
    
    
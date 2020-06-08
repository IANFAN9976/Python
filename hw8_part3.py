# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:07:05 2019

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
    
    at = bfield.at
    at1 = list(map(list,at))
    rt = bfield.rt
    ab = bfield.ab
    rb = bfield.rb
    bb = bfield.berry
    
    i = 0
    #continue to move the bears until it satisfies certain requirements
    while True:
        i += 1
        print()
        print('Turn: {}'.format(i))        
        bfield.grow()    
        for b in ab:
            b_bear = bear(b)
            if len(b) == 3 and b[:2] not in at1:
                b.append(0)
           
            elif len(b) == 4:
                b[3] = 0
                
            if b[:2] not in at1 and len(b) == 4:
                b[3] += bb[b[0]][b[1]]
                bb[b[0]][b[1]] = 0
                while b[3] < 30 and b[0] in range(len(bb)) and b[1] in range(len(bb)):
                    b_bear.move()
                    b[0] = b_bear.row
                    b[1] = b_bear.column
                    if b[:2] in at1:
                        
                        b.append(3)
                        break
                    else:
                        if b[0] in range(len(bb)) and b[1] in range(len(bb)):
                            dif = min(bb[b[0]][b[1]], 30-b[3])
                            b[3] += dif
                            bb[b[0]][b[1]] -= dif                
                        
            elif len(b) == 3:
                b.append(0)
                b.append(3)
                
        ab1 = ab.copy()
        for b in ab1:
            if b[0] not in range(len(bb)) or b[1] not in range(len(bb)):
                print(str(bear(b)) + ' - Left the Field')
                ab.remove(b) 
                
        for t in at:
            if len(t) == 2:
                t.append(0)
            
        for t in at:
            leave = False
            seen = 0     
            for b in ab :
                if t[:2] == b[:2] and t[:2] in at1:
                    print(str(tourist(t, t[2])) + ' - Left the Field')
                    at1.remove(t[:2])
                    leave = True
                    break
                    
                if (b[0]-t[0])**2 + (b[1] - t[1])**2 <= 16:
                    seen += 1
            if seen >= 3:
                print(str(tourist(t, t[2])) + ' - Left the Field')
                at1.remove(t[:2])
                leave = True
                break
            
            if leave:
                continue
            
            if seen == 0:
                t[2] += 1
            elif seen != 0:
                t[2] = 0
                
            if t[2] > 2:
                print(str(tourist(t, t[2])) + ' - Left the Field')
                at1.remove(t[:2])
        at2 = []
        for t in at:
            if t[:2] in at1:
                at2.append(t)
        bfield.at = at2
        at = at2
        #when there still have more 500 berries and reserve bears, add one bear into the field
        if bfield.total()[0] > 500 and len(rb) > 0:
            rb[0].append(0)
            ab1.append(rb[0])
            print(str(bear(rb[0])) + ' - Entered the Field')
            ab.append(rb[0])           
            ab1.append(rb[0])
            rb.remove(rb[0])
        #if there still have active bears and reserve tourist, add one tourist into the field
        if len(rt) > 0 and len(ab) > 0:
            at1.append(rt[0].copy())
            rt[0].append(0)
            print(str(tourist(rt[0], rt[0][2]))+ ' - Entered the Field')
            at.append(rt[0])
            rt.remove(rt[0])
        
    
        #if there's no active bears or no berries and no reserve bear, print out the information and break       
        if len(ab)==0 and len(rb)==0 or len(ab)==0 and bfield.total()[0]==0:
            print()
            print(bfield.total()[1])
            print(str(bfield))
    
            print('Active Bears:')
            print()
            print('Active Tourists:')
            for t in at2:
                print(str(tourist(t, t[2])))
            break
        #for each five turns, print out the information of active bears and active tourists
        if i%5 == 0:
            print(bfield.total()[1])
            print(str(bfield))
            print('Active Bears:')
            for b in ab:
                if len(b) == 4:
                    print(str(bear(b)))
    
            print()
            print('Active Tourists:')
            for t in at2:
                print(str(tourist(t, t[2])))
            
        else:
            for b in ab:            
                if len(b) == 5:
                    b[4] -= 1
                    if b[4] == 0:
                        b.pop()
        print()    



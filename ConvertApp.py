# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:43:36 2022

@author: erenk
"""

from math import *


def convert():
    choose = input("Type one (1) for convert binary to decimal, type two (2) for convert decimal to binary.  ")
    
    if choose == "1":
        binary = input("Type the binary (Only 1 and 0)  ")
    
        decimal=0
        force=0
    
        binarylist = list(binary)
        binarylen = len(binarylist)
        binaryindex= binarylen-1
    
    
    
            
        while binaryindex >= 0:
            value = (2**(force))*int((binarylist[binaryindex]))
            decimal = decimal + value
            binaryindex -= 1
            force += 1
        print("")    
        print("Decimal value of your input is: " + str(decimal))
    
    elif choose == "2":
        
        sayi = input("Type the decimal ")
        sayi = int(sayi)
    
        binarylist = [ ]
    
        a=0
    
        while a==0: 
        
            eleman = sayi % 2
        
            binarylist.append(eleman)
        
            sayi = sayi/2
        
            sayi = floor(sayi)
        
            if sayi == 0:
            
                a=1
    
        binarylist.reverse()
    
        bs = " ".join(str(x) for x in binarylist)
        print("")
        print("Binary value of your input is: " + bs)
        
    again = input("Type 'C' if you want convert another one or type 'Q' for quit:   ")
    if again=="c" or again=="C":
        convert()
    else:
        return 0
    
        
convert()
    



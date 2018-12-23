# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:06:10 2018

@author: 程甜甜
"""

def found ():
    xiaotou = ['A','B','C','D']
    #for(xiaotou='A';xiaotou<='D';xiaotou++):
    for xiaotou in ['A','B','C','D']:
        if(((xiaotou!='A')+(xiaotou=='D')+(xiaotou=='B')+(xiaotou!='D'))==1):
            print('小偷为'+xiaotou)
            #print(xiaotou)
        
found ()
    
    
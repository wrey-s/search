# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:11:35 2024

@author: wrey
"""
import os

#function for search
def search(files, search_box):
    #access and list files
    for file in os.listdir(files):
        #counter
        i=1 
        with open(os.path.join(files, file), 'r', encoding='utf-8') as filee:
            for str in filee:
                if search_box in (str:=str.title()):
                    print(f'result:{str}*****found in {file}*****line={i}')
                i+=1
    print()            
    print('end of search')
    print()
    
while True:
    #box for search
    search_box = input('enter a word for search:  ')
    #file address
    files = 'data/dickens'
    #recall function
    search(files , (search_box:=search_box.title()))
        
           
        
        

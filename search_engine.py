# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:11:35 2024

@author: wrey
"""
import os
import time

while True:
    def search(files, search_box): # تابع برای سرچ
        global start_time
        start_time = time.time() #زمان شروع اجرا 
        for file in os.listdir(files): # دسترسی و لیست فایل ها    
            i=1 #شمارنده
            with open(os.path.join(files, file), 'r', encoding='utf-8') as filee:
                for str in filee:
                    if search_box in (str:=str.title()):
                        print(f'result:{str}*****found in {file}*****line={i}')
                    i+=1
        print()            
        print('end of search')
        
    #باکس سرچ    
    search_box = input('enter a word for search:  ')
    #آدرس فایل    
    files = 'data/dickens'
    #فراخوانی تابع    
    search(files , (search_box:=search_box.title()))
    
    end_time = time.time()  # زمان پایان اجرا
    execution_time = end_time - start_time  # زمان اجرا
    print(f"Search time: {execution_time:.2f} seconds")
    print()
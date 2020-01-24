# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:01:51 2019

@author: Aviral Gaur
"""

import multiprocessing 
import time

start = time.perf_counter()

def do_something(seconds):
    print(f' sleeping {seconds} seconds')
    time.sleep(seconds)
    print('Done sleeping')
    
processes = []

#   '_' is a throw varable 
for _ in range (10):
    p = multiprocessing.Process(target=do_something, args=[2])
    p.start()
    processes.append(p)
    
for process in processes:
    process.join()
    
finish = time.perf_counter()

timer = {round(finish-start, 2)}
print(timer)

#print(f' Finished in  seconds')

    

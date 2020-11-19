# Date: 11/15/2020  
# Class: CS4541  
# Assignment: Assignment 3 - Memory Allocation  
# Author(s): Darryl Ming Sen Lee 

class Heap:

    def __init__(self):
        
        self.initialHeapsize=1000
        self.paddingData=255
        self.data=170
        self.startHeapPointer=1
        self.heap_array=[0]*self.initialHeapsize
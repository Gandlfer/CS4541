# Date: 10/23/2020  
# Class: CS4541  
# Assignment: Assignment 1 - Cache Simulator  
# Author(s): Darryl Ming Sen Lee 

from Block import Block
from Queue import Queue

#Class that is shaped like a cache without its functions
class Set:
    def __init__(self,s,e,b):
        self.maxsize=e
        self.cacheSystem=[Queue()for x in range(2**s)]#An array of Queue(initially it is empty)

    #returns all tags only in a list
    def listOfTag(self,sIndex):
        ls=[]
        for x in self.cacheSystem[sIndex].ls:
            ls.append(x.get_tag())
        return ls
    
    #check if eviction is needed
    def eviction(self,sIndex,blockdata,flag):
        #Only if eviction needed
        if(flag):
            self.cacheSystem[sIndex].dequeue()
        self.cacheSystem[sIndex].enqueue(blockdata)
    
    #returns boolean if queue is full
    def queueFull(self,sIndex):
        return self.cacheSystem[sIndex].get_size()==self.maxsize

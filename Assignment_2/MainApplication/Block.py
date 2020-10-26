# Date: 10/23/2020  
# Class: CS4541  
# Assignment: Assignment 2 - Cache Simulator  
# Author(s): Darryl Ming Sen Lee 

#class for one single block
class Block:
    def __init__(self,b_size):
        self.tag=0
        self.valid=0

    #return the tag address
    def get_tag(self):
        return self.tag

    #set the tag address
    def set_tag(self,tag):
        self.tag=tag

    #returns 1 or 0
    def get_valid(self):
        return self.valid

    #toggles valid to 1 or 0
    def set_valid(self):
        self.valid=self.valid^1

 

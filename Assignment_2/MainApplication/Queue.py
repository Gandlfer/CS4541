#Queue class to implement first in first out (FIFO) for Eviction
class Queue:
    def __init__(self):
        self.ls=[]

    #remove the first element in the array
    def dequeue(self):
        return self.ls.pop(0)
 
    #add the new element at the back of the array
    def enqueue(self,block):
        self.ls.append(block)
    
    #returns the current size of the queue
    def get_size(self):
        return len(self.ls)

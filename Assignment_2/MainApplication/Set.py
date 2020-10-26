from Block import Block
from Queue import Queue
class Set:
    def __init__(self,s,e,b):
        self.maxsize=e
        self.cacheSystem=[Queue()for x in range(2**s)]

    def listOfTag(self,sIndex):
        ls=[]
        for x in self.cacheSystem[sIndex].ls:
            ls.append(x.get_tag())
        return ls
        
    def eviction(self,sIndex,blockdata,flag):
        if(flag):
            self.cacheSystem[sIndex].dequeue()
        self.cacheSystem[sIndex].enqueue(blockdata)
            
    def queueFull(self,sIndex):
        return self.cacheSystem[sIndex].get_size()==self.maxsize

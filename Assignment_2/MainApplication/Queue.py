class Queue:
    def __init__(self):
        self.ls=[]

    def dequeue(self):
        return self.ls.pop(0)

    def enqueue(self,block):
        self.ls.append(block)
    
    def get_size(self):
        return len(self.ls)

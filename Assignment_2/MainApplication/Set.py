from Block import Block

class Set:
    def __init__(self,s,e,b):
        self.arr2D=[[Block(2**b)for x in range(e)]for x in range(2**s)]

if __name__=="__main__":
    temp=Set(3,2,2)
    print(temp.cache[2][0].valid)
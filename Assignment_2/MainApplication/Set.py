from Block import Block
from Queue import Queue
class Set:
    def __init__(self,s,e,b):
        self.maxsize=e
        #self.q=Queue(e)
        self.cacheSystem=[Queue()for x in range(2**s)]

    def listOfTag(self,sIndex):
        ls=[]
        for x in self.cacheSystem[sIndex].ls:
            ls.append(x.get_tag())
        return ls
        
    def eviction(self,sIndex,blockdata,incCount):
        evictionMsg=""
        if(self.cacheSystem[sIndex].get_size()==self.maxsize):
            self.cacheSystem[sIndex].dequeue()
            incCount+=1
            evictionMsg="eviction"
        self.cacheSystem[sIndex].enqueue(blockdata)

        return evictionMsg

if __name__=="__main__":
    #q=Queue(3)
    # arr=[Queue(3)for x in range(2**2)]
    # #ls=[1,2,3]
    # arr[0].enqueue(1)
    # print(len(arr[0].ls))
    arr=[0]*3
    arr[2]=1
    print(arr)
    #print(q)
    # string="6"
    # hexnum=int(string,16)
    # print(hexnum)
    # print(hexnum&3)
    # print(hexnum>>2)
    #temp=Set(3,2,2)
    #temp[0].a
    #print(temp.listOfTag(1))
    # temp.arr2D[2][0].set_valid()
    # print(temp.arr2D[2][0].get_valid())
    # temp.arr2D[2][0].set_valid()
    # print(temp.arr2D[2][0].get_valid())
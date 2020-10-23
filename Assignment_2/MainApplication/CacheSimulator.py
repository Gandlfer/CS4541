from Set import Set

class CacheSim:
    def __init__(self,s,e,b):
        self.hitCount=0
        self.missCount=0
        self.eviction=0
        self.cache=Set(s,e,b)
        #self.s=s
        #self.s_size=2**s
        #self.e=e
        #self.b=b
        #self.b_size=2**b
        #self.cache=np.zeros((s_size,b_size*e))
        self.result=[]
        return
    
    def readProcess(self,ls):
        for x in ls:
            
        return result

    def __load__(self,hexaddress,byte):
        return None

    def __store__(self,hexaddress,byte):
        return None

    def _modify__(self,hexaddress,byte):
        return None


from Set import Set

class CacheSim:
    def __init__(self,s,e,b):
        self.hitCount=0
        self.missCount=0
        self.eviction=0
        self.cache=Set(s,e,b)
        self.s=s
        self.e=e
        self.b=b
        #self.b_size=2**b
        #self.cache=np.zeros((s_size,b_size*e))
        self.result=[]
        return
    
    def readProcess(self,ls):
        result=[]
        for x in ls:
            splitted=x.split(" ")
            operation=splitted[2].split(",")
            #hexaddr=operation[0]
            op_addr=self.convertHextoInstruction(operation[0])
            getbyte=operation[1]
            if(splitted[1]=="L"):
                value=self.__load__(op_addr,getbyte)
            elif(splitted[1]=="S"):
                value=self.__store__(op_addr,getbyte)
            elif(splitted[1]=="M"):
                value=self.__modify__(op_addr,getbyte)
            result.append(value)

        return result

    def __load__(self,op,byte):
        self.cache[op[1]]
        return None

    def __store__(self,op,byte):
        return None

    def _modify__(self,op,byte):
        return None

    def convertHextoInstruction(self,hexaddress):
        operationInDecimal=int(hexaddress,16)
        offset=operationInDecimal&(2**self.b -1)
        operationInDecimal=operationInDecimal>>self.b
        sIndex=operationInDecimal&(2**self.s -1)
        operationInDecimal=operationInDecimal>>self.s
        tag=operationInDecimal
        return [tag,sIndex,offset]
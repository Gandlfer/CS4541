from Set import Set
from Block import Block
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
            getbyte=int(operation[1])
            if(splitted[1]=="L"):
                value=self.__load__(op_addr,getbyte)
            elif(splitted[1]=="S"):
                value=self.__store__(op_addr,getbyte)
            elif(splitted[1]=="M"):
                value=self.__modify__(op_addr,getbyte)
            print(x + value)
            print("\n")
            result.append(value)

        return result

    def __load__(self,op,byte):
        
        if(op[0] in self.cache.listOfTag(op[1])):
            indexWithTag=self.cache.listOfTag(op[1]).index(op[0])
            print(f"Tag={op[0]} set={op[1]}")
            print(f"{type(self.cache)}")
            if(self.cache[op[1]].ls[indexWithTag].get_valid()==1):
                self.hitCount+=1
                return " hit "

            else:
                self.cache[op[1]].ls[indexWithTag].set_valid()
                self.cache[op[1]].ls[indexWithTag].set_byte(op[2],byte)
                return " miss "

        b=Block(2**self.b)
        b.set_valid()
        b.set_tag(op[0])
        b.set_byte(op[2],byte)
        return " miss "+self.cache.eviction(op[1],b)


    def __store__(self,op,byte):
        if(op[0] in self.cache.listOfTag(op[1])):
            print(f"Tag={op[0]} set={op[1]}")
            print(f"{type(self.cache)}")
            #print(f"{type(self.cache[op[1]])}")
            indexWithTag=self.cache.listOfTag(op[1]).index(op[0])
            if(self.cache[op[1]].ls[indexWithTag].get_valid()==1):
                self.hitCount+=1
                return " hit "

            else:
                self.cache[op[1]].ls[indexWithTag].set_valid()
                self.cache[op[1]].ls[indexWithTag].set_byte(op[2],byte)
                return " miss "

        b=Block(2**self.b)
        b.set_valid()
        b.set_tag(op[0])
        b.set_byte(op[2],byte)
        return " miss "+self.cache.eviction(op[1],b)

    def _modify__(self,op,byte):
        return self.__load__(op,byte) + self.__store__(op,byte)

    def convertHextoInstruction(self,hexaddress):
        operationInDecimal=int(hexaddress,16)
        offset=operationInDecimal&(2**self.b -1)
        operationInDecimal=operationInDecimal>>self.b
        sIndex=operationInDecimal&(2**self.s -1)
        operationInDecimal=operationInDecimal>>self.s
        tag=operationInDecimal
        return [tag,sIndex,offset]
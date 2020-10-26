from Set import Set
from Block import Block
import sys
class CacheSim:
    def __init__(self,s,e,b):
        self.hitCount=0
        self.missCount=0
        self.evictionCount=0
        self.cache=Set(s,e,b)
        self.s=s
        self.e=e
        self.b=b
        return
    
    def readProcess(self,ls):
        result=[]
        value=""
        for x in ls:
            skip=False
            splitted=x.split(" ")
            #print(splitted)
            if(len(splitted)>3 or len(splitted)<3 or(splitted[1]!="L" and splitted[1]!="S" and splitted[1]!="M")):
                skip=True
            else:
                operation=splitted[2].split(",")
                lower_operation=operation[0].lower()

            for char in lower_operation:
                if(not((ord(char)>=48 and ord(char)<=57) or (ord(char)>=97 and ord(char)<=102))):
                    skip=True
                    break
            if (skip):
                result.append("Invalid Address")
                continue

            op_addr=self.convertHextoInstruction(lower_operation)
            getbyte=int(operation[1])
            print(splitted[1])
            if(splitted[1]=="L"):
                value=self.__load__(op_addr,getbyte)
            elif(splitted[1]=="S"):
                value=self.__store__(op_addr,getbyte)
            elif(splitted[1]=="M"):
                value=self.__modify__(op_addr,getbyte)

            #print(type(self.cache.cacheSystem[0]))
            #print(self.cache.cacheSystem[1].ls)
            #print(self.cache.cacheSystem[2].ls)
            #print(self.cache.cacheSystem[3].ls)
            for x in self.cache.cacheSystem:
                print(x.ls)
                for k in x.ls:
                    print(k.get_tag())
            result.append(value)

        return result

    def __load__(self,op,byte):
        print("Load")
        print(f"Finding Tag{op[0]}from Sindex{op[1]}")
        if(op[0] in self.cache.listOfTag(op[1])):
            print("Tag Found")
            indexWithTag=self.cache.listOfTag(op[1]).index(op[0])
            if(self.cache.cacheSystem[op[1]].ls[indexWithTag].get_valid()==1):
                print("Valid Block Found")
                self.hitCount+=1
                return " hit "

            else:
                print("Valid Block Not Found----Set")
                self.cache.cacheSystem[op[1]].ls[indexWithTag].set_valid()
                self.missCount+=1

                return " miss "

        print(f"Miss---Tag Not Found")
        self.missCount+=1
        b=Block(2**self.b)
        b.set_valid()
        b.set_tag(op[0])

        if(self.cache.queueFull(op[1])):
            print(f"Eviction")
            self.cache.eviction(op[1],b,True)  
            self.evictionCount+=1
            return " miss eviction"
        self.cache.eviction(op[1],b,False)

        return " miss "


    def __store__(self,op,byte):
        print("Store")
        print(f"Finding Tag{op[0]}from Sindex{op[1]}")
        if(op[0] in self.cache.listOfTag(op[1])):
            print("Tag Found")
            indexWithTag=self.cache.listOfTag(op[1]).index(op[0])
            if(self.cache.cacheSystem[op[1]].ls[indexWithTag].get_valid()==1):
                print("Valid Block Found")
                self.hitCount+=1
                return " hit "

            else:
                print("Valid Block Not Found----Set")
                self.cache.cacheSystem[op[1]].ls[indexWithTag].set_valid()
                self.missCount+=1
                return " miss "

        print(f"Miss---Tag Not Found")
        self.missCount+=1
        b=Block(2**self.b)
        b.set_valid()
        b.set_tag(op[0])

        if(self.cache.queueFull(op[1])):
            print(f"Eviction")        
            self.cache.eviction(op[1],b,True)
            self.evictionCount+=1
            return " miss eviction"
        self.cache.eviction(op[1],b,False)

        return " miss "

    def __modify__(self,op,byte):
        return self.__load__(op,byte) + self.__store__(op,byte)

    def convertHextoInstruction(self,hexaddress):
        #print(hexaddress)
        operationInDecimal=int(hexaddress,16)
        offset=operationInDecimal&(2**self.b -1)
        operationInDecimal=operationInDecimal>>self.b
        sIndex=operationInDecimal&(2**self.s -1)
        operationInDecimal=operationInDecimal>>self.s
        tag=operationInDecimal
        return [tag,sIndex,offset]
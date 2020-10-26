# Date: 10/23/2020  
# Class: CS4541  
# Assignment: Assignment 1 - Cache Simulator  
# Author(s): Darryl Ming Sen Lee 

from Set import Set
from Block import Block
import sys
#Class to take action to the cache
class CacheSim:
    def __init__(self,s,e,b):
        self.hitCount=0
        self.missCount=0
        self.evictionCount=0
        self.cache=Set(s,e,b)#Set the cache shaped object
        self.s=s
        self.e=e
        self.b=b
    
    #Read each instruction
    def readProcess(self,ls):
        result=[]
        value=""

        #looping through each instruction
        for x in ls:
            skip=False
            splitted=x.split(" ")#Splitting the instruction by the spaces as delimiter
            
            #Validation if it is a operation
            if(len(splitted)>3 or len(splitted)<3 or(splitted[1]!="L" and splitted[1]!="S" and splitted[1]!="M")):
                #Skip if it is not operation
                skip=True

            else:
                operation=splitted[2].split(",")
                lower_operation=operation[0].lower()
            
            #check if address is non hexadecimals
            for char in lower_operation:
                if(not((ord(char)>=48 and ord(char)<=57) or (ord(char)>=97 and ord(char)<=102))):
                    #Skip if it is not hexadecimals
                    skip=True
                    break
            
            #Skipping the loop based on previous flag
            if (skip):
                result.append("Invalid Address")
                continue
            
            #Get string to int to hexadecimal
            op_addr=self.convertHextoInstruction(lower_operation)

            if(splitted[1]=="L" or splitted[1]=="S"):
                value=self.__load__(op_addr)

            elif(splitted[1]=="S"):
                value=self.__load__(op_addr)

            elif(splitted[1]=="M"):
                value=self.__load__(op_addr)+self.__load__(op_addr)

            result.append(value)

        return result

    def __load__(self,op):
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


    def __store__(self,op):

        if(op[0] in self.cache.listOfTag(op[1])):
            indexWithTag=self.cache.listOfTag(op[1]).index(op[0])

            if(self.cache.cacheSystem[op[1]].ls[indexWithTag].get_valid()==1):
                self.hitCount+=1
                return " hit "

            else:
                self.cache.cacheSystem[op[1]].ls[indexWithTag].set_valid()
                self.missCount+=1
                return " miss "

        self.missCount+=1
        b=Block(2**self.b)
        b.set_valid()
        b.set_tag(op[0])

        if(self.cache.queueFull(op[1])):      
            self.cache.eviction(op[1],b,True)
            self.evictionCount+=1
            return " miss eviction"

        self.cache.eviction(op[1],b,False)

        return " miss "

    def __modify__(self,op):
        return self.__load__(op) + self.__store__(op)

    def convertHextoInstruction(self,hexaddress):
        operationInDecimal=int(hexaddress,16)
        offset=operationInDecimal&(2**self.b -1)
        operationInDecimal=operationInDecimal>>self.b
        sIndex=operationInDecimal&(2**self.s -1)
        operationInDecimal=operationInDecimal>>self.s
        tag=operationInDecimal
        return [tag,sIndex,offset]
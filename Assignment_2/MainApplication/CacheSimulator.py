# Date: 10/23/2020  
# Class: CS4541  
# Assignment: Assignment 2 - Cache Simulator  
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
            #check for type of operation
            if(splitted[1]=="L" or splitted[1]=="S"):
                value=self.__loadAndstore__(op_addr)

            elif(splitted[1]=="M"):
                value=self.__loadAndstore__(op_addr)+self.__loadAndstore__(op_addr)
            
            #append the result as string into a list 
            result.append(value)

        return result

    def __loadAndstore__(self,op):

        #find if tag is in any block
        if(op[0] in self.cache.listOfTag(op[1])):
            #if found, find the index for the block
            indexWithTag=self.cache.listOfTag(op[1]).index(op[0])
            
            #Check if block is valid
            if(self.cache.cacheSystem[op[1]].ls[indexWithTag].get_valid()==1):
                #if block is valid, inc hitCount return hit
                self.hitCount+=1

                return " hit "
            
            else:
                #if block invalid,set it to valid, inc missCount return miss
                self.cache.cacheSystem[op[1]].ls[indexWithTag].set_valid()
                self.missCount+=1

                return " miss " 
        
        #if tag not found, inc missCount
        #create a new block
        self.missCount+=1
        b=Block(2**self.b)
        b.set_valid()
        b.set_tag(op[0])

        #check if eviction is needed
        if(self.cache.queueFull(op[1])):
            #Eviction if E is full and inc evictionCount return miss and eviction
            self.cache.eviction(op[1],b,True)  
            self.evictionCount+=1

            return " miss eviction"
        
        #no eviction needed
        self.cache.eviction(op[1],b,False)

        return " miss "

    #convert string to int and changes it to hexadecimal
    def convertHextoInstruction(self,hexaddress):
        operationInDecimal=int(hexaddress,16)#Changes to hex
        offset=operationInDecimal&(2**self.b -1)#bit mask the number of bits for offset
        operationInDecimal=operationInDecimal>>self.b#bit shift the number of bits to the right
        sIndex=operationInDecimal&(2**self.s -1)#bit mask the number of bits for set
        operationInDecimal=operationInDecimal>>self.s#bit shift the number of bits to the right
        tag=operationInDecimal#Remainding value is tag

        return [tag,sIndex,offset]
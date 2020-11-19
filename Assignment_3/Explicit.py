# Date: 11/15/2020  
# Class: CS4541  
# Assignment: Assignment 3 - Memory Allocation  
# Author(s): Darryl Ming Sen Lee 

from HeapClass import Heap
import sys

class Explicit(Heap):

    def __init__(self,fitType):
        super().__init__()
        self.fitType=fitType
        #self.topPointer=0
        self.root=None
        self.nextOffset=1
        self.prevOffset=2

    # takes an integer value indicating the number of bytes to allocate for the payload of the block
    #   returns a "pointer" to the starting address of the payload of the allocated block
    #   The "pointer" above can take any form you like, depending on the data structure you use to represent your heap
    def myalloc(self,size):
        pointer=0

        #find the closest number to 8
        allocating_size=size+8
        maskValue=allocating_size & 7
        shiftedAllocated_size=allocating_size>>3
        if(maskValue>0):
            shiftedAllocated_size=shiftedAllocated_size+1
        shiftedAllocated_size=int((shiftedAllocated_size<<3)/4)

        if(self.fitType==0):

            pointer=self.firstFit(shiftedAllocated_size)

        else:

            pointer=self.bestFit(shiftedAllocated_size)

        
        padding=shiftedAllocated_size*4-allocating_size
        allocating_size=allocating_size-8
        
        for x in range(pointer+1,pointer+shiftedAllocated_size-1):

            if(allocating_size>=4):

                allocating_size=allocating_size-4
                self.heap_array[x]=2863311530

            elif(allocating_size>0):

                for y in range(allocating_size):
                    self.heap_array[x]=self.heap_array[x]+self.data*256**(y)

                remaindingPadding=4-allocating_size

                for y in range(allocating_size,allocating_size+remaindingPadding):

                    self.heap_array[x]=self.heap_array[x]+self.paddingData*256**(y)
                
                allocating_size=0

                padding=padding-remaindingPadding

            elif(padding>=4):
                padding=padding-4
                self.heap_array[x]=4294967295
        
        return pointer

    #takes a pointer to an allocated block and an integer value to resize the block to
    #   returns a "pointer" to the new block 
    #   frees the old block
    #   a call to myrealloc with a size of zero is equivalent to a call to myfree    
    def myrealloc(self, pointer, size):
        newpointer=0
        self.myfree(pointer)

        if(size!=0):
            newpointer=self.myalloc(size)

            return newpointer

        else:

            return None

    def bestFit(self,size):
        temproot=self.root
        pointer_toSmallestBlock=0 
        smallestSize=sys.maxsize
        while(1):
            if(temproot==None and smallestSize!=sys.maxsize):
                smallestBlockHeader=self.heap_array[pointer_toSmallestBlock]
                smallestnextBlock=self.heap_array[pointer_toSmallestBlock+1]
                smallestprevBlock=self.heap_array[pointer_toSmallestBlock+2]
                #currentBlockSize=self.get_size(currentBlockHeader)
                data=size<<1
                self.heap_array[pointer_toSmallestBlock]=data
                self.heap_array[pointer_toSmallestBlock-1+size]=data
                self.toggleAllocatedBit(pointer_toSmallestBlock)
                self.toggleAllocatedBit(pointer_toSmallestBlock-1+size)

                leftOverSize=smallestSize-size
                pointer_ToLeftOverHeader=pointer_toSmallestBlock+size
                data=leftOverSize<<1
                self.heap_array[pointer_ToLeftOverHeader]=data
                self.heap_array[pointer_ToLeftOverHeader+leftOverSize-1]=data
                if(leftOverSize>2):
                    self.heap_array[pointer_ToLeftOverHeader+1]=smallestnextBlock
                    self.heap_array[pointer_ToLeftOverHeader+2]=smallestprevBlock
                    if(smallestprevBlock==None):
                        root=pointer_ToLeftOverHeader
                    else:
                        self.heap_array[smallestprevBlock+1]=pointer_ToLeftOverHeader

                    if(smallestnextBlock!=None):
                        self.heap_array[smallestnextBlockk+2]=pointer_ToLeftOverHeader

                return temproot
            elif(temproot==None and smallestSize==sys.maxsize):
                #not found
                temproot=self.findEnd(size)
                data=size<<1
                self.heap_array[temproot]=data
                self.heap_array[temproot-1+size]=data
                self.toggleAllocatedBit(temproot)
                self.toggleAllocatedBit(temproot-1+size)

                return temproot

            elif(self.get_size(self.heap_array[temproot])==size):
                self.toggleAllocatedBit(temproot)
                self.toggleAllocatedBit(temproot-1+size)
                currentBlockHeader=self.heap_array[temproot]
                nextBlock=self.heap_array[temproot+1]
                prevBlock=self.heap_array[temproot+2]

                if(prevBlock==None):
                    root=nextBlock
                else:
                    self.heap_array[prevBlock+1]=nextBlock

                if(nextBlock!=None):
                    self.heap_array[nextBlock+2]=prevBlock

                return temproot

            elif(self.get_size(self.heap_array[temproot])>size and self.get_size(self.heap_array[temproot])<smallestSize):
                pointer_toSmallestBlock=temproot
                smallestSize=self.get_size(self.heap_array[temproot])
                
            temproot=self.heap_array[temproot+1]
            
        return temproot

    def firstFit(self,size):
        temproot=self.root

        while(1):
            print(temproot)
            if(temproot==None):
                #not found
                temproot=self.findEnd(size)
                data=size<<1
                self.heap_array[temproot]=data
                self.heap_array[temproot-1+size]=data
                self.toggleAllocatedBit(temproot)
                self.toggleAllocatedBit(temproot-1+size)


            elif(self.get_size(self.heap_array[temproot])==size):
                self.toggleAllocatedBit(temproot)
                self.toggleAllocatedBit(temproot-1+size)
                currentBlockHeader=self.heap_array[temproot]
                nextBlock=self.heap_array[temproot+1]
                prevBlock=self.heap_array[temproot+2]

                if(prevBlock==None):
                    root=nextBlock
                else:
                    self.heap_array[prevBlock+1]=nextBlock

                if(nextBlock!=None):
                    self.heap_array[nextBlock+2]=prevBlock

                break

            elif(self.get_size(self.heap_array[temproot])>size):
                
                currentBlockHeader=self.heap_array[temproot]
                nextBlock=self.heap_array[temproot+1]
                prevBlock=self.heap_array[temproot+2]
                currentBlockSize=self.get_size(currentBlockHeader)
                data=size<<1
                self.heap_array[temproot]=data
                self.heap_array[temproot-1+size]=data
                self.toggleAllocatedBit(temproot)
                self.toggleAllocatedBit(temproot-1+size)

                leftOverSize=currentBlockSize-size
                pointer_ToLeftOverHeader=temproot+size
                data=leftOverSize<<1
                self.heap_array[pointer_ToLeftOverHeader]=data
                self.heap_array[pointer_ToLeftOverHeader+leftOverSize-1]=data
                if(leftOverSize>8):
                    self.heap_array[pointer_ToLeftOverHeader+1]=nextBlock
                    self.heap_array[pointer_ToLeftOverHeader+2]=prevBlock
                    if(prevBlock==None):
                        root=pointer_ToLeftOverHeader
                    else:
                        self.heap_array[prevBlock+1]=pointer_ToLeftOverHeader

                    if(nextBlock!=None):
                        self.heap_array[nextBlock+2]=pointer_ToLeftOverHeader

                break
                
            else:
                temproot=self.heap_array[temproot+1]
            
        return temproot

    # frees the block pointed to by the input parameter "pointer"
    #   returns nothing
    #   only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
    #   otherwise, does not change the heap
    def myfree(self, pointer):
        if(self.get_allocated(self.heap_array[pointer])==0):

            print("Block is not allocated. No free action is taken.\n")

        else:

            allocated_size=self.get_size(self.heap_array[pointer])
            self.toggleAllocatedBit(pointer)
            self.toggleAllocatedBit(pointer+allocated_size-1)

            self.zeroBlock(pointer,allocated_size)
            temproot=self.root
            previous=None
            while(1):
                if(temproot==None and previous==None):

                    self.root=pointer
                    self.heap_array[pointer+1]=None
                    self.heap_array[pointer+2]=None
                    break

                elif(temproot==None and previous!=None):
                    self.heap_array[pointer+1]=None
                    self.heap_array[pointer+2]=previous

                    self.heap_array[previous+1]=pointer
                    break

                elif(temproot>pointer):
                    tempnext=self.heap_array[temproot+self.nextOffset]
                    tempprev=self.heap_array[temproot+self.prevOffset]
                    self.heap_array[temproot+self.prevOffset]=pointer
                    self.heap_array[pointer+self.nextOffset]=temproot
                    self.heap_array[pointer+self.prevOffset]=tempprev
                    if (tempprev!=None):
                        self.heap_array[tempprev+self.nextOffset]=pointer

                    break

                previous=temproot
                temproot=self.heap_array[temproot+1]

            self.bicoalescing(pointer)
        
    # grows or shrinks the size of the heap by a number of words specified by the input parameter "size"
    # you may call this whenever you need to in the course of a simulation, as you need to grow the heap
    # this call will return an error and halt the simulation if your heap would need to grow past the maximum size of 100,000 words
    def mysbrk(self, size):

        if(self.initialHeapsize+size<=100000):

            extend_array=[0]*size
            self.heap_array[self.initialHeapsize-1:self.initialHeapsize-1]=extend_array
            self.initialHeapsize=self.initialHeapsize+size

        else:

            print("Error! Heap can't grow past 100000 words")
            exit()

    #check if there is empty allocated block at the back and front and merge them together 
    def bicoalescing(self,pointer):
 
        # get the starting pointer for header and footer of the current block
        pointer_currentBlockHeader=pointer
        pointer_currentBlockNext=pointer+self.nextOffset
        pointer_currentBlockPrev=pointer+self.prevOffset
        currentBlockSize=self.get_size(self.heap_array[pointer])
        pointer_currentBlockFooter=pointer+currentBlockSize-1

        #check previous block for empty allocated block
        if(pointer!=1):#if it is 1st array in the list, it is empty
            
            # previous's block footer
            pointer_previousBlockFooter=pointer-1
            previousBlockFooter=self.heap_array[pointer_previousBlockFooter]
        
            if(self.get_allocated(previousBlockFooter)==0): # check if it is allocated
                
                # get data from previous block 
                previousBlockSize=self.get_size(previousBlockFooter)
                pointer_previousBlockHeader=pointer_previousBlockFooter-previousBlockSize+1
                pointer_previousBlockNext=pointer_previousBlockHeader+self.nextOffset
                pointer_previousBlockPrev=pointer_previousBlockHeader+self.prevOffset

                newBlockSize=previousBlockSize+currentBlockSize

                currentBlockSize=newBlockSize
                newBlockSize=newBlockSize<<1 

                self.heap_array[pointer_previousBlockHeader]=newBlockSize # replace the header of previous block to become the current header block
                self.heap_array[pointer_currentBlockFooter]=newBlockSize # update the current footer block to the new size
                self.heap_array[pointer_previousBlockNext]=self.heap_array[pointer_currentBlockNext]
                if(self.heap_array[pointer_currentBlockNext]!=None):
                    self.heap_array[self.heap_array[pointer_currentBlockNext]+self.prevOffset]=pointer_previousBlockHeader

                self.heap_array[pointer_previousBlockFooter]=0 # clear the previous block footer 
                self.heap_array[pointer]=0 # clear the current block header
                self.heap_array[pointer+self.nextOffset]=0
                self.heap_array[pointer+self.prevOffset]=0

                pointer_currentBlockHeader=pointer_previousBlockHeader # change the pointer from the previous block header to current block header
                pointer_currentBlockNext=pointer_previousBlockNext
                
        #check next block for empty allocated block
        if(pointer_currentBlockFooter+1!=self.get_heapSize()-1): #end of heap

            if(self.heap_array[pointer_currentBlockFooter+1]!=0): #check if it next block is not allocated
                # next block footer
                pointer_nextBlockHeader=pointer_currentBlockFooter+1
                nextBlockHeader=self.heap_array[pointer_nextBlockHeader]

                if(self.get_allocated(nextBlockHeader)==0): # check if it is allocated
                    
                    nextBlockSize=self.get_size(nextBlockHeader)
                    pointer_nextBlockFooter=pointer_nextBlockHeader+nextBlockSize-1
                    pointer_nextBlockNext=pointer_nextBlockHeader+self.nextOffset
                    pointer_nextBlockPrev=pointer_nextBlockHeader+self.prevOffset

                    newBlockSize=nextBlockSize+currentBlockSize

                    currentBlockSize=newBlockSize
                    newBlockSize=newBlockSize<<1 # generate data for new block

                    self.heap_array[pointer_currentBlockHeader]=newBlockSize
                    self.heap_array[pointer_nextBlockFooter]=newBlockSize
                    self.heap_array[pointer_currentBlockNext]=self.heap_array[pointer_nextBlockNext]
                    if(self.heap_array[pointer_currentBlockNext]!=None):
                        self.heap_array[self.heap_array[pointer_currentBlockNext]+self.prevOffset]=pointer_currentBlockHeader

                    self.heap_array[pointer_nextBlockHeader]=0 # clear the next block Header 
                    self.heap_array[pointer_currentBlockFooter]=0 # clear the current block footer
                    self.heap_array[pointer_nextBlockHeader+self.nextOffset]=0
                    self.heap_array[pointer_nextBlockHeader+self.prevOffset]=0

    # convert string of hexadecimal to int
    def hexToDecimal(self,hexa):
        return int(hexa,16)

    # clear a block from start pointer and how many blocks should be cleared
    def zeroBlock(self,pointer,size):
        for x in range(pointer+1,pointer+size-1):
            self.heap_array[x]=0

    # bit shift to the right by 1 bit for the int size number
    def get_size(self,number):
        return number >> 1

    # Mask most right bit to check for allocated
    def get_allocated(self,number):
        return number & 1

    # XOR the most right bit for on or off
    def toggleAllocatedBit(self,pointer):
        self.heap_array[pointer]=self.heap_array[pointer]^1

    # get the size of the current heap
    def get_heapSize(self):
        return len(self.heap_array)

    def findEnd(self,size):
        pointer=1
        while(1):
            if(pointer+size>self.get_heapSize()):
                self.mysbrk(size)

            if(self.heap_array[pointer]==0):
                return pointer

            else:
                pointer=pointer+self.get_size(self.heap_array[pointer])

    def writeHeap(self):
        fileName="output.txt"
        openFile=open(fileName,"w")
        for x in range(len(self.heap_array)):
            openFile.write(f"{x}, {self.decimalToHex(self.heap_array[x])}\n")
        openFile.close()
#if __name__=="__main__":
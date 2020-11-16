from HeapClass import Heap
import sys

class Implicit(Heap):

    def __init__(self,fitType):
        super().__init__()
        self.fitType=fitType

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

        tempSize=size

        for x in range(pointer+1,pointer+shiftedAllocated_size-1):

            if(tempSize/4>=1):#stored data

                tempSize=tempSize-4
                self.heap_array[x]=2863311530

            else:

                for y in range(tempSize):#stored data by byte

                    self.heap_array[x]=self.heap_array[x]+self.data*32**(y)

                for y in range(4-tempSize):#padding

                    self.heap_array[x]=self.heap_array[x]+self.paddingData*32**(y)
        
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

        empty=True

        pointer=self.startHeapPointer
        pointer_toSmallestBlock=0 
        smallestSize=sys.maxsize
        pointer_toFooter=0
        allocated_size=0

        while(empty):
            
            if(pointer+size==self.initialHeapsize-1):

                mysbrk(size)

            #not found
            if(self.heap_array[pointer]==0 and smallestSize==sys.maxsize):

                pointer_toFooter=pointer-1+size
                
                data=size<<1
                self.heap_array[pointer]=data
                self.heap_array[pointer_toFooter]=data
                self.toggleAllocatedBit(pointer)
                self.toggleAllocatedBit(pointer_toFooter)

                return pointer

            #end and no smallest found
            elif(self.heap_array[pointer]==0 and smallestSize!=sys.maxsize):

                empty=False

                data=size<<1
                self.heap_array[pointer_toSmallestBlock]=data
                self.heap_array[pointer_toSmallestBlock+size-1]=data
                self.toggleAllocatedBit(pointer_toSmallestBlock)
                self.toggleAllocatedBit(pointer_toSmallestBlock+size-1)

                pointer=pointer_toSmallestBlock
                pointer_toFooter=pointer_toSmallestBlock+size-1

            else:

                allocated_size=self.get_size(self.heap_array[pointer])

                if(self.get_allocated(self.heap_array[pointer])==0):

                    if(allocated_size==size):

                        self.toggleAllocatedBit(pointer)
                        self.toggleAllocatedBit(pointer+size-1)
                        return pointer

                    elif(allocated_size>size and allocated_size<smallestSize):

                        pointer_toSmallestBlock=pointer
                        smallestSize=allocated_size
                        
                pointer=pointer+allocated_size

        pointer_toLeftOverHeader=pointer_toFooter+1
        newSize=allocated_size-size

        if(newSize>=2):
            
            data=newSize<<1
            self.heap_array[pointer_toLeftOverHeader]=data
            self.heap_array[pointer_toLeftOverHeader+newSize-1]=data

        return pointer

    def firstFit(self,size):

        empty=True
        pointer=self.startHeapPointer
        pointer_toFooter=0
        allocated_size=0

        while(empty):
            
            if(pointer+size==self.initialHeapsize-1):
                mysbrk(size)

            #if allocated block dont have that size
            #create new allocatedblock
            if(self.heap_array[pointer]==0):

                pointer_toFooter=pointer-1+size
                data=size<<1
                self.heap_array[pointer]=data
                self.heap_array[pointer_toFooter]=data
                self.toggleAllocatedBit(pointer)
                self.toggleAllocatedBit(pointer_toFooter)
                
                return pointer

            #get each allocated block
            else:

                allocated_size=self.get_size(self.heap_array[pointer])

                if(self.get_allocated(self.heap_array[pointer])==0): 

                    if(allocated_size>=size):

                        pointer_toFooter=pointer+size-1
                        data=size<<1
                        self.heap_array[pointer]=data
                        self.heap_array[pointer_toFooter]=data
                        self.toggleAllocatedBit(pointer)
                        self.toggleAllocatedBit(pointer_toFooter)
                        break

                pointer=pointer+allocated_size

        pointer_toLeftOverHeader=pointer_toFooter+1
        newSize=allocated_size-size

        if(newSize>=2):

            data=newSize<<1
            self.heap_array[pointer_toLeftOverHeader]=data
            self.heap_array[pointer_toLeftOverHeader+newSize-1]=data

        return pointer

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
                newBlockSize=previousBlockSize+currentBlockSize

                currentBlockSize=newBlockSize
                newBlockSize=newBlockSize<<1 

                self.heap_array[pointer_previousBlockHeader]=newBlockSize # replace the header of previous block to become the current header block
                self.heap_array[pointer_currentBlockFooter]=newBlockSize # update the current footer block to the new size

                self.heap_array[pointer_previousBlockFooter]=0 # clear the previous block footer 
                self.heap_array[pointer]=0 # clear the current block header

                pointer_currentBlockHeader=pointer_previousBlockHeader # change the pointer from the previous block header to current block header
                
        #check next block for empty allocated block
        if(pointer_currentBlockFooter+1!=self.get_heapSize()-1): #end of heap

            if(self.heap_array[pointer_currentBlockFooter+1]!=0): #check if it next block is not allocated
                # next block footer
                pointer_nextBlockHeader=pointer_currentBlockFooter+1
                nextBlockHeader=self.heap_array[pointer_nextBlockHeader]

                if(self.get_allocated(nextBlockHeader)==0): # check if it is allocated
                    
                    nextBlockSize=self.get_size(nextBlockHeader)
                    pointer_nextBlockFooter=pointer_nextBlockHeader+nextBlockSize-1
                    newBlockSize=nextBlockSize+currentBlockSize

                    currentBlockSize=newBlockSize
                    newBlockSize=newBlockSize<<1 # generate data for new block

                    self.heap_array[pointer_currentBlockHeader]=newBlockSize
                    self.heap_array[pointer_nextBlockFooter]=newBlockSize

                    self.heap_array[pointer_nextBlockHeader]=0 # clear the next block Header 
                    self.heap_array[pointer_currentBlockFooter]=0 # clear the current block footer

    # convert string of hexadecimal to int
    def hexToDecimal(self,hexa):
        return int(hexa,16)

    # clear a block from start pointer and how many blocks should be cleared
    def zeroBlock(self,pointer,size):
        for x in range(pointer+1,pointer+size-1):
            self.heap_array[x]=0

    # bit shift the the right by 1 bit for the int size number
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

    def printHeap(self):

        pointer=self.startHeapPointer
        allocated_size=0
        while(1):

            if(self.heap_array[pointer]==0):
                break

            else:

                allocated_size=self.get_size(self.heap_array[pointer])
                pointer_toFooter=pointer+allocated_size-1
                print(f"Header: at index {pointer} value={self.heap_array[pointer]} size={allocated_size} allocated={self.get_allocated(self.heap_array[pointer])}")
                for x in range(pointer+1,pointer_toFooter):
                    print(f"Value={self.heap_array[x]}")
                    print("Per byte: ")
                    temp=self.heap_array[x]
                    for y in range(4):
                        value=temp&255
                        temp=temp>>8
                        print(f"{y} Byte={value}")
                print(f"Footer: at index {pointer_toFooter} value={self.heap_array[pointer_toFooter]}")

                pointer=pointer+allocated_size
#if __name__=="__main__":

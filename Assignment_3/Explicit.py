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
        allocating_size=size+2
        maskValue=allocating_size & 1
        shiftedAllocated_size=allocating_size>>1
        if(maskValue>0):
            shiftedAllocated_size+1
        shiftedAllocated_size=shiftedAllocated_size<<1
        #padding=2-maskValue
        if(fitType==0):
            pointer=self.firstFit(shiftedAllocated_size)

        else:
            pointer=self.bestFit(shiftedAllocated_size)

        for x in range(pointer+1,pointer+shiftedAllocated_size-1):
            self.heap_array[pointer]=4294967295

        if(maskValue==1):
            self.heap_array[pointer+shiftedAllocated_size-2]=2863311530

        return pointer

    #takes a pointer to an allocated block and an integer value to resize the block to
    #   returns a "pointer" to the new block 
    #   frees the old block
    #   a call to myrealloc with a size of zero is equivalent to a call to myfree    
    def myrealloc(self, pointer, size):
        newpointer=0
        return newpointer

    def bestFit(self,size):
        empty=True
        #pointer=self.startHeapPointer+1
        pointer=self.startHeapPointer
        pointer_toSmallestBlock=0 
        smallestSize=sys.maxsize
        while(empty):
            
            if(pointer+size==self.initialHeapsize-1):
                mysbrk(size)

            if(self.heap_array[pointer]==0 and smallestSize==sys.maxsize):
                #empty=False
                pointer_toFooter=pointer-1+size
                
                # self.splitValue(data,pointer)
                # self.splitValue(data,pointer_toFooter)
                # self.toggleAllocatedBit(pointer)
                # self.toggleAllocatedBit(pointer_toFooter)
                data=self.toggleAllocatedBit(size<<1)
                self.heap_array[pointer]=data
                self.heap_array[pointer_toFooter]=data
                
                return pointer

            elif(self.heap_array[pointer]==0 and smallestSize!=sys.maxsize):
                empty=False

                self.toggleAllocatedBit(self.heap_array[pointer_toSmallestBlock])
                self.toggleAllocatedBit(self.heap_array[pointer_toSmallestBlock+smallestSize-1])

            else:
                #header=hexToDecimal(makeWordBlock(pointer,pointer+3))
                #header=self.makeWordBlock(pointer)
                #allocated=header & 1
                #pointer_toSmallestBlock=0  
                allocated_size=self.get_size(self.heap_array[pointer])
                if(self.get_allocated(self.heap_array[pointer])==0):
                    if(allocated_size==size):
                        self.toggleAllocatedBit(self.heap_array[pointer])
                        self.toggleAllocatedBit(self.heap_array[pointer+allocated_size-1])
                        return pointer

                    elif(allocated_size>size and allocated_size<smallestSize):
                        #self.toggleAllocatedBit(pointer)
                        #self.toggleAllocatedBit(pointer+allocated_size-4)
                        #return pointer
                        pointer_toSmallestBlock=pointer
                        smallestSize=allocated_size
                        

                pointer=pointer+allocated_size

        return pointer_toSmallestBlock

    def firstFit(self,size):
        empty=True
        pointer=self.startHeapPointer

        while(empty):
            
            if(pointer+size==self.initialHeapsize-1):
                mysbrk(size)

            if(self.heap_array[pointer]==0):

                pointer_toFooter=pointer-1+size

                data=self.toggleAllocatedBit(size<<1)
                self.heap_array[pointer]=data
                self.heap_array[pointer_toFooter]=data
                
                return pointer
   
            else:
                #header=hexToDecimal(makeWordBlock(pointer,pointer+3))
                #header=self.makeWordBlock(pointer)
                #allocated=header & 1
                allocated_size=self.get_size(self.heap_array[pointer])
                if(self.get_allocated(self.heap_array[pointer])==0): 
                    if(allocated_size>=size):
                        self.toggleAllocatedBit(self.heap_array[pointer])
                        self.toggleAllocatedBit(self.heap_array[pointer+allocated_size-1])
                        return pointer

                pointer=pointer+allocated_size

    # frees the block pointed to by the input parameter "pointer"
    #   returns nothing
    #   only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
    #   otherwise, does not change the heap
    def myfree(self, pointer):
        #header=hexToDecimal(makeWordBlock(pointer,pointer+3))
        #header=self.makeWordBlock(pointer)
        # allocated=header & 1

        #if(self.get_allocated(header)==0):
        if(self.get_allocated(self.heap_array[pointer])==0):
            print("Block is not allocated. No free action is taken.\n")

        else:
            #allocated_size=self.get_size(header)
            allocated_size=self.get_size(self.heap_array[pointer])
            self.toggleAllocatedBit(self.heap_array[pointer])
            self.toggleAllocatedBit(self.heap_array[pointer+allocated_size-1])

            self.zeroBlock(pointer,allocated_size)
            #self.splitValue(0,pointer+4,allocated_size-8)
            # for x in range(pointer+4,pointer+allocated_size-4):
            #     self.heap_array[x]=0

            self.bicoalescing(pointer)
        
# grows or shrinks the size of the heap by a number of words specified by the input parameter "size"
# you may call this whenever you need to in the course of a simulation, as you need to grow the heap
# this call will return an error and halt the simulation if your heap would need to grow past the maximum size of 100,000 words
    def mysbrk(self, size):
        if(self.initialHeapsize+size<=100000):
            #extend_array=[0]*self.wordByte*size
            extend_array=[0]*size
            self.heap_array[self.initialHeapsize-1:self.initialHeapsize-1]=extend_array
            self.initialHeapsize=self.initialHeapsize+size
            #self.heap_array.extend(extend_array)

        else:
            print("Error! Heap can't grow past 100000 words")
            exit()

    def bicoalescing(self,pointer):
        # pointer_currentBlockHeader=pointer
        # currentBlockHeader=self.makeWordBlock(pointer)
        # currentBlockSize=self.get_size(currentBlockHeader)
        # pointer_currentBlockFooter=pointer+currentBlockSize-self.wordByte
        # currentBlockFooter=self.makeWordBlock(pointer_currentBlockFooter)
        currentBlockSize=self.get_size(self.heap_array[pointer])
        pointer_currentBlockFooter=pointer+currentBlockSize-1

        #check behind of current block for empty memory
        if(pointer!=4):
            #pointer_previousBlockFooter=pointer-self.wordByte
            #previousBlockFooter=self.makeWordBlock(pointer_previousBlockFooter)
            pointer_previousBlockFooter=pointer-1
            previousBlockFooter=self.heap_array[pointer_previousBlockFooter]
            if(self.get_allocated(previousBlockFooter)==0):
            #if(self.get_allocated(self.heap_array[pointer_previousBlockFooter])==0):
                previousBlockSize=self.get_size(previousBlockFooter)
                pointer_previousBlockHeader=pointer_previousBlockFooter-previousBlockSize+1
                newBlockSize=previousBlockSize+currentBlockSize

                currentBlockSize=newBlockSize

                newBlockSize=newBlockSize<<1
                
                #self.splitValue(newBlockSize,pointer_previousBlockHeader)
                #self.splitValue(newBlockSize,pointer_currentBlockFooter)
                self.heap_array[pointer_previousBlockHeader]=newBlockSize
                self.heap_array[pointer_currentBlockFooter]=newBlockSize
                #self.splitValue(0,pointer_previousBlockFooter)
                #self.splitValue(0,pointer)
                self.heap_array[pointer_previousBlockFooter]=0
                self.heap_array[pointer]=0

                pointer_currentBlockHeader=pointer_previousBlockHeader
                
        if(pointer_currentBlockFooter+1!=self.get_heapSize-1): #end of heap
            #if(makeWordBlock(pointer_currentBlockFooter+4)!=0):
            if(self.heap_array[pointer_currentBlockFooter+1]!=0):
                pointer_nextBlockHeader=pointer_currentBlockFooter+1
                nextBlockHeader=self.heap_array[pointer_nextBlockHeader]
                if(self.get_allocated(nextBlockHeader)==0):
                    nextBlockSize=self.get_size(nextBlockHeader)
                    pointer_nextBlockFooter=pointer_nextBlockHeader+nextBlockSize-1
                    newBlockSize=nextBlockSize+currentBlockSize

                    currentBlockSize=newBlockSize

                    newBlockSize=newBlockSize<<1

                    # self.splitValue(newBlockSize,pointer_currentBlockHeader)
                    # self.splitValue(newBlockSize,pointer_nextBlockFooter)
                    self.heap_array[pointer_currentBlockHeader]=newBlockSize
                    self.heap_array[pointer_nextBlockFooter]=newBlockSize
                    # self.splitValue(0,pointer_nextBlockHeader)
                    # self.splitValue(0,pointer_currentBlockFooter)
                    self.heap_array[pointer_nextBlockHeader]=0
                    self.heap_array[pointer_currentBlockFooter]=0

                    #pointer_currentBlockHeader=pointer_previousBlockHeader

    def hexToDecimal(self,hexa):
        return int(hexa,16)

    # def splitValue(self,value,pointer,zero=0):

    #     for x in range(pointer,pointer+self.wordByte+zero):
    #         self.heap_array[x]=value%256**(x-pointer)
    #         value=value/256**(x-pointer)

    # def decimalToHex(self,dec):
    #     return hex(dec)

    # def makeWordBlock(self,start):
    #     hexa=0
    #     for x in range(start,start+self.wordByte):
    #         hexa+=self.heap_array[x]*256**(x-start)
    #     return hexa

    def zeroBlock(self,pointer,size):
        for x in range(pointer+1,pointer+size-1):
            self.heap_array[x]=0

    def get_size(self,address):
        mask=address & (2**32 -1-1)
        mask= mask >> 1
        return mask

    def get_allocated(self,address):
        #header=self.makeWordBlock(address)
        return address & 1

    def toggleAllocatedBit(self,pointer):
        self.heap_array[pointer]=self.heap_array[pointer]^1

    def get_heapSize(self):
        return len(self.heap_array)

if __name__=="__main__":
    heap=Heap()
    arr=[1,2,3]
    #arr.insert(1,(4,5,6))
    arr[2:2]=[4,5,6]
    print(arr)
    #heap.initialHeapsize=1000
    #print(round(0%10))
    #print("0x"+'{0:02b}'.format(0))
    #print(heap.hexToDecimal("0xfb3de83a")^1^1^1)
    #print(heap.hexToDecimal("0xfb3de83a"^1^1^1))
    #print(heap.get_size(heap.hexToDecimal("0xfb3de83a")))
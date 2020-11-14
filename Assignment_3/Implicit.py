from Assignment_3.HeapClass import Heap
class Implicit(Heap):
    # wordByte=4
    # alignment=8
    # initialHeapsize=1000
    # startHeapPointer=3
    # # endHeapPointer=3

    def __init__(self,fitType):
        super().__init__()
        self.fitType=fitType
        # self.wordByte=4
        # self.alignment=8
        # self.initialHeapsize=1000
        # self.startHeapPointer=3
        # self.endHeapPointer=3
        # heap_array=[0]*self.wordByte*self.initialHeapsize

    # takes an integer value indicating the number of bytes to allocate for the payload of the block
    #   returns a "pointer" to the starting address of the payload of the allocated block
    #   The "pointer" above can take any form you like, depending on the data structure you use to represent your heap
    def myalloc(self,size):
        pointer=0
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
        pointer=self.startHeapPointer+1

        while(empty):
            
            if(pointer+size==self.initialHeapsize-4):
                mysbrk(size)

            if(self.heap_array[pointer]==0):
                empty=False
                pointer_toFooter=pointer-4+size
                data=size<<1
                self.splitValue(data,pointer)
                self.splitValue(data,pointer_toFooter)
                self.toggleAllocatedBit(pointer)
                self.toggleAllocatedBit(pointer_toFooter)
   
            else:
                #header=hexToDecimal(makeWordBlock(pointer,pointer+3))
                header=self.makeWordBlock(pointer)
                #allocated=header & 1
                allocated_size=self.get_size(header)
                if(self.get_allocated(header)==0): 
                    if(allocated_size-(self.wordByte*2)==size):
                        self.toggleAllocatedBit(pointer)
                        self.toggleAllocatedBit(pointer+allocated_size-4)
                        return pointer

                pointer=pointer+allocated_size

        return pointer

    # frees the block pointed to by the input parameter "pointer"
    #   returns nothing
    #   only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
    #   otherwise, does not change the heap
    def myfree(self, pointer):
        #header=hexToDecimal(makeWordBlock(pointer,pointer+3))
        header=self.makeWordBlock(pointer)
        # allocated=header & 1

        if(self.get_allocated(header)==0):
            print("Block is not allocated. No free action is taken.\n")

        else:
            allocated_size=self.get_size(header)
            self.toggleAllocatedBit(pointer)
            self.toggleAllocatedBit(pointer+allocated_size-4)

            self.splitValue(0,pointer+4,allocated_size-8)
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
            self.initialHeapsize=self.initialHeapsize+size
            self.heap_array.extend(extend_array)

        else:
            print("Error! Heap can't grow past 100000 words")

    def bicoalescing(self,pointer):
        pointer_currentBlockHeader=pointer
        currentBlockHeader=self.makeWordBlock(pointer)
        currentBlockSize=self.get_size(currentBlockHeader)
        pointer_currentBlockFooter=pointer+currentBlockSize-self.wordByte
        currentBlockFooter=self.makeWordBlock(pointer_currentBlockFooter)
        
        #check behind of current block for empty memory
        if(pointer!=4):
            pointer_previousBlockFooter=pointer-self.wordByte
            previousBlockFooter=self.makeWordBlock(pointer_previousBlockFooter)
            if(self.get_allocated(previousBlockFooter)==0):
                previousBlockSize=self.get_size(previousBlockFooter)
                pointer_previousBlockHeader=pointer_previousBlockFooter-previousBlockSize+4
                newBlockSize=previousBlockSize+currentBlockSize

                currentBlockSize=newBlockSize

                newBlockSize=newBlockSize<<1
                self.splitValue(newBlockSize,pointer_previousBlockHeader)
                self.splitValue(newBlockSize,pointer_currentBlockFooter)
                self.splitValue(0,pointer_previousBlockFooter)
                self.splitValue(0,pointer)

                pointer_currentBlockHeader=pointer_previousBlockHeader
                
        if(pointer_currentBlockFooter+4!=self.get_heapSize-4): #end of heap
            if(makeWordBlock(pointer_currentBlockFooter+4)!=0):
                pointer_nextBlockHeader=pointer_currentBlockFooter+self.wordByte
                nextBlockHeader=self.makeWordBlock(pointer_nextBlockHeader)
                if(self.get_allocated(nextBlockHeader)==0):
                    nextBlockSize=self.get_size(nextBlockHeader)
                    pointer_nextBlockFooter=pointer_nextBlockHeader+previousBlockSize-4
                    newBlockSize=nextBlockSize+currentBlockSize

                    currentBlockSize=newBlockSize

                    newBlockSize=newBlockSize<<1
                    self.splitValue(newBlockSize,pointer_currentBlockHeader)
                    self.splitValue(newBlockSize,pointer_nextBlockFooter)
                    self.splitValue(0,pointer_nextBlockHeader)
                    self.splitValue(0,pointer_currentBlockFooter)
                    #pointer_currentBlockHeader=pointer_previousBlockHeader

    def hexToDecimal(self,hexa):
        return int(hexa,16)

    def splitValue(self,value,pointer,zero=0):

        for x in range(pointer,pointer+self.wordByte+zero):
            self.heap_array[x]=value%256**(x-pointer)
            value=value/256**(x-pointer)

    # def decimalToHex(self,dec):
    #     return hex(dec)

    def makeWordBlock(self,start):
        hexa=0
        for x in range(start,start+self.wordByte):
            hexa+=self.heap_array[x]*256**(x-start)
        return hexa

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
    #heap.initialHeapsize=1000
    #print(round(0%10))
    #print("0x"+'{0:02b}'.format(0))
    #print(heap.hexToDecimal("0xfb3de83a")^1^1^1)
    #print(heap.hexToDecimal("0xfb3de83a"^1^1^1))
    #print(heap.get_size(heap.hexToDecimal("0xfb3de83a")))
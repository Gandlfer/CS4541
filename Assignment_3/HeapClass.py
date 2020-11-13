class Heap:
    wordByte=4
    alignment=8
    initialHeapsize=1000
    startHeapPointer=3
    endHeap=3

    def __init__(self):
        heap_array=[0]*self.wordByte*self.initialHeapsize

    # takes an integer value indicating the number of bytes to allocate for the payload of the block
    # returns a "pointer" to the starting address of the payload of the allocated block
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
        pointer=startHeapPointer+1

        while(empty):

            if(self.heap_array[pointer]==0):
                empty=False

            else: 
                header=hexToDecimal(makeBlock(pointer,pointer+3))
                allocated=header & 1
                allocated_size=get_size(header)
                if(allocated==0): 
                    if(allocated_size-1==size):
                        return pointer

                pointer=pointer+allocated_size+1

        return pointer

# frees the block pointed to by the input parameter "pointer"
#   returns nothing
#   only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
#   otherwise, does not change the heap
    def myfree(self, pointer):
        header=hexToDecimal(makeBlock(pointer,pointer+3))
        allocated=header & 1

        if(allocated==0):
            print("Block is not allocated. No free action is taken.\n")

        else:
            allocated_size=get_size(header)
            toggleAllocatedBit(pointer)
            toggleAllocatedBit(pointer+4+allocated_size)

            for x in range(pointer+4,pointer+4+allocated_size):
                self.heap_array[x]=0

            bicoalescing(pointer)
        
# grows or shrinks the size of the heap by a number of words specified by the input parameter "size"
# you may call this whenever you need to in the course of a simulation, as you need to grow the heap
# this call will return an error and halt the simulation if your heap would need to grow past the maximum size of 100,000 words
    def mysbrk(self, size):
        if(self.initialHeapsize+size<=100000):
            extend_array=[0]*self.wordByte*size
            self.initialHeapsize=self.initialHeapsize+size
            self.heap_array.extend(extend_array)

        else:
            print("Error! Heap can't grow past 100000 words")
            exit()

    def bicoalescing(self,pointer):
        return 0

    def hexToDecimal(self,hexa):
        return int(hexa,16)

    # def decimalToHex(self,dec):
    #     return hex(dec)

    def makeBlock(self,start,end):
        hexa="0x"
        for x in range(end,start-1,-1):
            hexa=hexa+self.heap_array[x]
        return hexa

    def get_size(self,address):
        mask=address & (2**32 -1-1)
        mask= mask >> 1
        return mask

    def toggleAllocatedBit(self,pointer):
        self.heap_array[pointer]=self.heap_array[pointer]^1

if __name__=="__main__":
    heap=Heap()
    print("0x"+'{0:02b}'.format(0))
    #print(heap.hexToDecimal("0xfb3de83a")^1^1^1)
    #print(heap.hexToDecimal("0xfb3de83a"^1^1^1))
    #print(heap.get_size(heap.hexToDecimal("0xfb3de83a")))
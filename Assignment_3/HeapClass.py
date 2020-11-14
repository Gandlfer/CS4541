class Heap:
    # wordByte=4
    # alignment=8
    # initialHeapsize=1000
    # startHeapPointer=3
    # # endHeapPointer=3

    def __init__(self):
        self.wordByte=4
        self.alignment=8
        self.initialHeapsize=1000
        self.startHeapPointer=3
        self.endHeapPointer=3
        heap_array=[0]*self.wordByte*self.initialHeapsize
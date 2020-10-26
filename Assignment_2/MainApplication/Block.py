
class Block:
    def __init__(self,b_size):
        self.byte=[0]*b_size
        self.tag=0
        self.valid=0

    def get_tag(self):
        return self.tag

    def set_tag(self,tag):
        self.tag=tag

    def get_valid(self):
        return self.valid

    def set_valid(self):
        self.valid=self.valid^1

    def get_byte(self):
        return self.byte

    def set_byte(self,offset,readsize):
        print(f"From {offset} to {offset+readsize} max{len(self.byte)}")
        for x in range(offset,offset+readsize):
            print(f"{x}\n")
            self.byte[x]=1
 

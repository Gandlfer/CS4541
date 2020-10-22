
class Block:
    def __init__(self,b_size):
        self.byte=[0]*b_size
        self.tag=0
        self.valid=0

    @property
    def tag(self):
        return self.tag

    @property.setter
    def set_tag(self,tag):
        self.tag=tag

    @property
    def valid(self):
        return self.valid

    @property.setter
    def set_valid(self):
        valid=valid^1

    @property
    def byte(self):
        return self.byte

    @property.setter
    def set_byte(self,offset,data):
        for
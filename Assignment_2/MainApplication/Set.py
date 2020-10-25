from Block import Block

class Set:
    def __init__(self,s,e,b):
        self.arr2D=[[Block(2**b)for x in range(e)]for x in range(2**s)]

if __name__=="__main__":
    string="6"
    hexnum=int(string,16)
    print(hexnum)
    print(hexnum&3)
    print(hexnum>>2)
    # temp=Set(3,2,2)
    # temp.arr2D[2][0].set_valid()
    # print(temp.arr2D[2][0].get_valid())
    # temp.arr2D[2][0].set_valid()
    # print(temp.arr2D[2][0].get_valid())
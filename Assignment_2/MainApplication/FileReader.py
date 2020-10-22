import os

class FileReader:
    def __init__(self,path):
        self.path=path

    def __openfileObject__(self):
        fileOpen=open(self.path,"r")
        with fileOpen as f:
            print(f.read())

if __name__=="__main__":
    #print(cpath)
    FileReader("traces\\yi.trace").__openfileObject__()
    s="string"
    new_s=s.replace("s","t")
    print(s)
    print(new_s)
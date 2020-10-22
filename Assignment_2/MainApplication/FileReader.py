import os

class FileReader:
    def __init__(self,path):
        self.path=path

    def openFileObject(self):
        fileOpen=open(self.path,"r")
        ls=[]
        with fileOpen as f:
            data =f.read()
            print(data)
            if(data[0]!='I'):
                ls.append(data.replace("\n",""))
        return ls

# if __name__=="__main__":
#     #print(cpath)
#     FileReader("traces\\yi.trace").__openfileObject__()
#     s="string"
#     new_s=s.replace("s","t")
#     print(s)
#     print(new_s)
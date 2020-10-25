import os

class FileReader:
    def __init__(self,path):
        self.path=path

    def openFileObject(self):
        fileOpen=open(self.path,"r")
        ls=[]
        for x in fileOpen.readlines():
            if(x[0]!="I"):
                ls.append(x.replace("\n",""))
        return ls

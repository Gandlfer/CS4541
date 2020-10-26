import os

class FileReader:
    def __init__(self,path):
        self.path=path

    def openFileObject(self):
        try:
            fileOpen=open(self.path,"r")
        except(FileNotFoundError):
            print("File not found!\nCheck your file name and directory again!\n")
            os._exit(0)
        ls=[]
        for x in fileOpen.readlines():
            if(x[0]!="I" and x[0]!="\n"):
                ls.append(x.replace("\n",""))

        fileOpen.close()
        return ls

if __name__=="__main__":
    f=FileReader("traces/yi2.trace")
    f.openFileObject()
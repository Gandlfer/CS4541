import os

#class for read file
class FileReader:
    def __init__(self,path):
        self.path=path

    def openFileObject(self):
        #Exception Handling when file not found
        try:
            fileOpen=open(self.path,"r")#open file
        
        #Ends program when file not foud
        except(FileNotFoundError):
            print("File not found!\nCheck your file name and directory again!\n")
            os._exit(0)
        #create empty list
        ls=[]

        #Read file line by line
        for x in fileOpen.readlines():
            #Get only L M S 
            #if(x[1]=="L" or x[1]=="M" or x[1]=="S"):
            ls.append(x.replace("\n",""))

        fileOpen.close()#close file
        return ls
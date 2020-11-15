from FileReader import FileReader

import sys

if __name__=="__main__":
    #if(len(sys.argv)>=1):
    if(1):
        instruction=FileReader("Assignment_3\input.txt").openFileObject()#sys.argv[1]
        for x in instruction:
            print(x)

        listType=input("1 for Implicit\n2 for Explicit\nEnter:")
        fitType=input("1 for First Fit\n2 for Next Fit\nEnter:")
    else:
        print("Invalid format!\n")
        print("Usage: python3 Application.py <textfile_path>\n\t")
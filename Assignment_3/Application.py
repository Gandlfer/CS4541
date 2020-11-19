# Date: 11/15/2020  
# Class: CS4541  
# Assignment: Assignment 3 - Memory Allocation  
# Author(s): Darryl Ming Sen Lee 

from FileReader import FileReader
from Implicit import Implicit
from Explicit import Explicit

import sys

if __name__=="__main__":
    #if(len(sys.argv)>=1):
    if(1):

        stack={}

        instruction=FileReader("Assignment_3\input.txt").openFileObject()#sys.argv[1]
        heapType=None

        listType=input("0 for Implicit\n1 for Explicit\nEnter:")

        fitType=input("0 for First Fit\n1 for Best Fit\nEnter:")

        if(listType=="0"):

            heapType=Implicit(int(fitType))

        elif(listType=="1"):

            heapType=Explicit(fitType)

        for x in instruction:

            splitted=x.split(", ")

            if(splitted[0]=='a'):

                stack[splitted[2]]=heapType.myalloc(int(splitted[1]))

            elif(splitted[0]=='f'):

                heapType.myfree(stack[splitted[1]])
                stack[splitted[1]]=-1
                
            elif(splitted[0]=='r'):

                stack[splitted[3]]=heapType.myrealloc(stack[splitted[2]],int(splitted[1]))
                stack[splitted[2]]=-1

        heapType.writeHeap()

    else:

        print("Invalid format!\n")
        print("Usage: python3 Application.py <textfile_path>\n\t")
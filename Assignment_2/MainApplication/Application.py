import sys
from FileReader import FileReader
from CacheSimulator import CacheSim

#Main driver class that reads input and print result
if __name__=="__main__":
    #./csim-ref -s 4 -E 1 -b 4 -t traces/yi.trace
    #Make sure command arguments is not empty
    if(len(sys.argv)>=1):
        
        #check if every prefix exist 
        if(("v" in sys.argv[1] or "s" in sys.argv[1]) and "-s" in sys.argv and "-E" in sys.argv and "-b" in sys.argv and
            "-t" in sys.argv):
            #get the index of path based on prefix
            pathIndex=sys.argv.index("-t")+1

            #get all Load, Store and Modify operations only 
            calls=FileReader(sys.argv[pathIndex]).openFileObject()

            #check if -s -E -b are numbers only
            try:
                s=int(sys.argv[int(sys.argv.index("-s")+1)])
                e=int(sys.argv[int(sys.argv.index("-E")+1)])
                b=int(sys.argv[int(sys.argv.index("-b")+1)])
            except(ValueError):
                print("Invalid Value for -s -E -b")
                sys.exit(0)

            #check if -s -E -b are non-zero
            if(s>0 and e>0 and b>0):
                #create cache simulation
                cs=CacheSim(s,e,b)
                #read through the list of operation and return the hits, misses and evictions 
                result=cs.readProcess(calls)

                #if verbose flag is toggled
                if("v" in sys.argv[1]):
                    for x in range(len(calls)):
                        #print result paired with operation
                        print(f"{calls[x]} {result[x]}")
                
                #output the number of hits, misses and eviction
                print(f"Hit: {cs.hitCount} Miss: {cs.missCount} Eviction: {cs.evictionCount}")

            else:
                print("Set, Associativity and Block size cannot be 0")

        #Help Usage
        elif( "-h" in sys.argv[1]):
            print("Usage: python3 Application.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>\n\t"+
                        "-h: Optional help flag that prints usage info\n\t"+
                        "-v: Optional verbose flag that displays trace info\n\t"+
                        "-s <s>: Number of set index bits (S = 2 s is the number of sets)\n\t"+
                        "-E <E>: Associativity (number of lines per set)\n\t"+
                        "-b <b>: Number of block bits (B = 2 b is the block size)\n\t"+
                        "-t <tracefile>: Name of the valgrind trace to replay")

        #Error if missing any prefix
        else:
            print("Invalid simulation type!\nFor Usage info, do 'python3 Application.py -h'")

    else:
        print("Invalid format!\n")
        print("Usage: python3 Application.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>\n\t"+
                        "-h: Optional help flag that prints usage info\n\t"+
                        "-v: Optional verbose flag that displays trace info\n\t"+
                        "-s <s>: Number of set index bits (S = 2 s is the number of sets)\n\t"+
                        "-E <E>: Associativity (number of lines per set)\n\t"+
                        "-b <b>: Number of block bits (B = 2 b is the block size)\n\t"+
                        "-t <tracefile>: Name of the valgrind trace to replay")
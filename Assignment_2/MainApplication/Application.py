import sys
import Assignment_2.MainApplication.FileReader as FileReader
import Assignment_2.MainApplication.CacheSimulator as CacheSim
if __name__=="__main__":
    #./csim-ref -s 4 -E 1 -b 4 -t traces/yi.trace
    if(len(sys.argv)>=1):
        pathIndex=sys.argv.index("-t")+1
        calls=FileReader(sys.argv[pathIndex]).openFileObject()
        #cs=CacheSim(calls)
        #Print step by step for cache
        if("v" in sys.argv[1]):
            for x in calls:
                print(x)

        #Help Usage
        elif( "h" in sys.argv[1]):
            print("Usage: python3 Application.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>\n\t"+
                        "-h: Optional help flag that prints usage info\n\t"+
                        "-v: Optional verbose flag that displays trace info\n\t"+
                        "-s <s>: Number of set index bits (S = 2 s is the number of sets)\n\t"+
                        "-E <E>: Associativity (number of lines per set)\n\t"+
                        "-b <b>: Number of block bits (B = 2 b is the block size)\n\t"+
                        "-t <tracefile>: Name of the valgrind trace to replay\n")

        #Normal mode
        elif("s" in sys.argv[1]):
            print()

        else:
            print("Invalid simulation type!\n")
    else:
        print("Invalid format!\n")
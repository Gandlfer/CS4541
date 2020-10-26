import sys
from FileReader import FileReader
from CacheSimulator import CacheSim
if __name__=="__main__":
    #./csim-ref -s 4 -E 1 -b 4 -t traces/yi.trace
    if(len(sys.argv)>=1):
        
        if(("v" in sys.argv[1] or "s" in sys.argv[1]) and "-s" in sys.argv and "-E" in sys.argv and "-b" in sys.argv and
            "-t" in sys.argv):
            pathIndex=sys.argv.index("-t")+1
            calls=FileReader(sys.argv[pathIndex]).openFileObject()
            try:
                s=int(sys.argv[int(sys.argv.index("-s")+1)])
                e=int(sys.argv[int(sys.argv.index("-E")+1)])
                b=int(sys.argv[int(sys.argv.index("-b")+1)])
            except(ValueError):
                print("Invalid Value for -s -E -b\n")
                sys.exit(0)

            cs=CacheSim(s,e,b)
            result=cs.readProcess(calls)
            #if("v" in sys.argv[1]):
                #for x in range(len(calls)):
                    #print(f"{calls[x]} {result[x]}")
            print(f"Hit: {cs.hitCount} Miss: {cs.missCount} Eviction: {cs.evictionCount}")
            
        #Help Usage
        elif( "-h" in sys.argv[1]):
            print("Usage: python3 Application.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>\n\t"+
                        "-h: Optional help flag that prints usage info\n\t"+
                        "-v: Optional verbose flag that displays trace info\n\t"+
                        "-s <s>: Number of set index bits (S = 2 s is the number of sets)\n\t"+
                        "-E <E>: Associativity (number of lines per set)\n\t"+
                        "-b <b>: Number of block bits (B = 2 b is the block size)\n\t"+
                        "-t <tracefile>: Name of the valgrind trace to replay\n")

        else:
            print("Invalid simulation type!\n")
    else:
        print("Invalid format!\n")
import sys

def singleletter(l):
    return ord(l)-64

def stringtonumber(s):
    length = len(s)
    n = 0
    for i in range(length):
        n = n+ singleletter(s[length-i-1]) *(26 **i)
    return n

def main():
    print stringtonumber(sys.argv[1])
    
if __name__ =='__main__':
    main()
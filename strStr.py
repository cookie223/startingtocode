import sys


def strStr(haystack,needle):
    try:
        return haystack.index(needle)
    except:
        return -1

if __name__=="__main__":
    if len(sys.argv)==3:
        print strStr(sys.argv[1],sys.argv[2])
    else :
        print "Invalid input"
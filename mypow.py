import sys


def mypow(x, n):
    if x is not None and n is not None:
        return x ** n
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print mypow(float(sys.argv[1]), float(sys.argv[2]))
    else:
        print "invalid number of arguments"

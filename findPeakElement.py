import sys

def findPeakElement(num):
    'Should be in logarithmic complexity..Someday'
    if num[0] > num[1]:
        return 0
    elif num[-1]>num[-2]:
        return len(num)-1
    else:
        for i in range(len(num)-2):
            if num[i] < num[i+1] and num[i+2] < num[i+1]:
                return i+1
                break

def main():
    print findPeakElement(sys.argv[1])

if __name__=='__main__':
    main()
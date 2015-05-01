import sys


def addBinary(a, b):
    'return bin(int(a,2)+int(b,2))[2:]'
    sumtemp = str(a + b)
    sumlist = []
    for char in sumtemp:
        sumlist.append(int(char))
    for i in range(1, len(sumtemp) + 1):
        if sumlist[-i] == 0 or sumlist[-i] == 1:
                pass
        else:
            if i + 1 < len(sumtemp) + 1:
                if sumlist[-i] == 2:
                    sumlist[-i] = 0
                    sumlist[-i - 1] += 1
                else:
                    sumlist[-i] = 1
                    sumlist[-i - 1] += 1
            else:
                if sumlist[-i] == 2:
                    sumlist[-i] = 0
                    sumlist.insert(0, 1)
                else:
                    sumlist[-i] = 1
                    sumlist.insert(0, 1)
    return "".join(str(x) for x in sumlist)


if __name__ == '__main__':
    print(addBinary(int(sys.argv[1]), int(sys.argv[2])))

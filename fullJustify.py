from math import ceil

words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
L = 16

words2 = ['a', 'b', 'c', 'd']
L2 = 1

words3 = ['What', 'must', 'be', 'shall', 'be.']
L3 = 12

words4 = ["Here","is","an","example","of","text","justification."]
L4 = 14


def fullJustify(words, maxWidth):
    'distribute blanks evenly'
    lines = []
    L = 0
    ltemp = []
    i = 0
    lastlinemarker = False
    while i < len(words):
        while L + len(words[i]) <= maxWidth:
            # REALLY SHOULD THINK THROUGH +1? may < is better
            L = L + len(words[i]) + 1
            ltemp.append(words[i])
            # print len(words[i])
            # print L
            i += 1
            if i >= len(words):
                lastlinemarker = True
                break
        nblanks = maxWidth - L + len(ltemp)
        # print i, L, ltemp
        if len(ltemp) == 1:
            lines.append(ltemp[0] + nblanks * ' ')
        elif len(ltemp) == 0:
            raise Exception
        else:
            wtemp = ''
            if lastlinemarker:
                sword = " ".join(ltemp)
                sblanks = maxWidth - len(sword)
                lines.append(sword + sblanks * ' ')
            else:

                for j in range(len(ltemp)):
                    # print j
                    # print nblanks
                    if not nblanks == 0:
                        nb1 = ceil(float(nblanks) / (len(ltemp) - j - 1))
                    else:
                        nb1 = 0
                    wtemp = wtemp + ltemp[j] + int(nb1) * ' '
                    nblanks -= int(nb1)
                    # print nb1
                lines.append(wtemp)
                wtemp = ''
                nb1 = 0
                j = 0
        nblanks = 0
        L = 0
        ltemp = []
        # print lines
    return lines


print fullJustify(words4, L4)

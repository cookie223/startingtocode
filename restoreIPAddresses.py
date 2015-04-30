input1 = '25525511135'


def restorepart(s, n):
    validmarker = True
    list = []
    if not n == 0:
        if not (len(s) >= n and len(s) <= 3*n):
            validmarker = False
            return (validmarker, )
        else:
            if not s[0] <= 2:
                validmarker = False
                return (validmarker, )
            else:
                while i in range(1, 4):
                    if restorepart(s[i:], n-1)[1]:
                        list[n] = s[:i+1]


def restoreIPAddresses(s):
    result = []
    

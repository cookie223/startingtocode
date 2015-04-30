a = []


def singleNum(nums):
    'one single, others triple'
    if not nums:
        return None
    numdict = {}
    for i in nums:
        if numdict.get(i, 0) == 0:
            numdict[i] = 1
        elif numdict.get(i, 0) == 1:
            numdict[i] = 2
        elif numdict.get(i, 0) == 2:
            del numdict[i]
    for numitem in numdict.items():
        return numitem[0]


if __name__ == '__main__':
    print(singleNum(a))

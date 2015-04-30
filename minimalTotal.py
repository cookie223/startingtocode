input1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]


def minimalTotal(triangle):
    'from bottom to top'
    if len(triangle) == 0:
        return 0
    bline = triangle.pop()
    while len(bline) > 1:
        aline = triangle.pop()
        for i in range(len(aline)):
            aline[i] = aline[i] + min(bline[i], bline[i+1])
        bline = aline
    return bline[0]

print minimalTotal(input1)

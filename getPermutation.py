import math


class Solution:
    # @param {intger} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        ilist = [i + 1 for i in range(n)]
        reslist = []
        while n > 1:
            nfact = math.factorial(n - 1)
            pos = (k - 1) // nfact
            reslist.append(ilist.pop(pos))
            n -= 1
            k = (k - 1) % nfact + 1
        reslist.append(ilist[0])
        return "".join((str(i) for i in reslist))

s = Solution()

print s.getPermutation(1, 1)
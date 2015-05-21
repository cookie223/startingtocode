
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if not nums:
            return []
        numdict = {}
        resdict = {}
        for num in nums:
            numdict[num] = numdict.get(num, 0) + 1
        numtuple = tuple(numdict.keys())
        for i in range(len(numtuple) - 1):
            a = numtuple[i]
            for j in range(i + 1, len(numtuple)):
                b = numtuple[j]
                if not a == b:
                    c = -a - b 
                    if numdict.get(c, -1) >(0 if c not in [a, b] else 1):
                        # deal with (-1, 2) but not a second (-1) condition, (0, 0, 0) not included
                        res = tuple(sorted([a, b, c]))
                        resdict[res] = resdict.get(res, 0) + 1
        if numdict.get(0, 0) >= 3:
            # (0, 0, 0) condition
            res = (0, 0, 0)
            resdict[res] = resdict.get(res, 0) + 1
        return resdict.keys()

s = Solution()
nums = [-1, 0, 1, 2, -1, 4]
print s.threeSum(nums)

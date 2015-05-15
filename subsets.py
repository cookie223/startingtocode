class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def resubset(self, sortnums):
        if len(sortnums) == 1:
            return [[], sortnums]
        else:
            a = [sortnums[0]]
            result = []
            for res in self.resubset(sortnums[1:]):
                result.append(res)
                result.append(a + res)
            return result


    def subsets(self, nums):
        'just sort and call the recursive method'
        if not nums:
            return [[]]
        nums.sort()
        return self.resubset(nums)

if __name__ == '__main__':
    s = Solution()
    testinput = [1]
    print s.subsets(testinput) 
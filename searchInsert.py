class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)
        if nums[0] >= target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        while low < high - 1:
            mid = (low + high)//2
            if nums[mid] == target:
                low = mid
                high = mid
                break
            elif nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid
        return high


nums = [1, 3, 5, 6]
targets = [0, 1, 2, 3, 4, 5, 6, 7]

s = Solution()
for target in targets:
    print s.searchInsert(nums, target),
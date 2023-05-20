class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        for i in xrange(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
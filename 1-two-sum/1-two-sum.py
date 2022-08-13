class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
          curr = nums[i] 
          require = target - curr 
          
          if require in (nums[i+1:]):
            for j in range(i+1, len(nums)):
              if nums[j] == require:
                return [i, j]
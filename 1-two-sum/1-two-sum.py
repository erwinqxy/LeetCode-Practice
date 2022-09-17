class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # precommute the array and check back 
      mappings = {} 
      for i in range (len(nums)):
        rem = target - nums[i] 
        if (rem in mappings): 
          return [i, mappings[rem]]
        if (nums[i] not in mappings):
          mappings[nums[i]] = i
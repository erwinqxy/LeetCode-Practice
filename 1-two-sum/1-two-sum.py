class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # precommute the array and check back 
      mappings = {} 
      for i in range (len(nums)):
        # get the value required for the second half 
        rem = target - nums[i] 
        # check if it already exist in the mapping, if exist great! 
        if (rem in mappings): 
          return [i, mappings[rem]]
        # else continue storing what you have seen 
        if (nums[i] not in mappings):
          mappings[nums[i]] = i
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      currRunningSum = 0 
      ans = [] 
      for i in range(len(nums)):
        currRunningSum += nums[i]
        ans.append(currRunningSum)
      return ans 
      
      
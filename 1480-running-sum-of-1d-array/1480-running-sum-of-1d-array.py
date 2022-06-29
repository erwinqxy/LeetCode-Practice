class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [] 
        accSum = 0 
        for i in range(0, len(nums)): 
            accSum += nums[i]
            ans.append(accSum)
        return ans
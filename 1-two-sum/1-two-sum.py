class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            n1 = nums[i] 
            n2_needToBe = target - n1 
            if (n2_needToBe in nums[i:]):
                for j in range(i+1, len(nums)):
                    n2 = nums[j]
                    if (n1 + n2 == target):
                        return [i, j]

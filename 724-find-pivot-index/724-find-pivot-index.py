class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #get the rightsum once 
        currRightSum = self.getRightSum(0, nums)
        currLeftSum = 0 
        for i in range (len(nums)): 
            if (currRightSum == currLeftSum):
                return i      
            else:
                if (i+1 == len(nums)):
                    return -1
                currRightSum -= nums[i+1]
                currLeftSum += nums[i] 
        return -1 

    
    def getRightSum(self, pivot, nums):
        ans = 0
        for i in range(pivot+1, len(nums)):
            ans += nums[i]
        return ans 
        
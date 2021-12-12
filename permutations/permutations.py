class Solution(object):
    # model this like a DFS problem 
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [] 
        self.dfs(nums, [], result)
        return result
    
    # dfs here used to recurse until the end 
    def dfs(self, nums, path, result): 
        if not nums:
            result.append(path)
            return 
        for i in range (len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]] , result)
        
        
        
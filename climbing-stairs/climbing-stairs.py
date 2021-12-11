class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #DS to help with the cache 
        cache = {} 
        
        # memo function 
        def helper(n):    
            if (n in cache):
                return cache[n]
            
            if n == 0:
                result = 0 
            elif n == 1:
                result = 1
            elif n == 2:
                result = 1 + helper(n-1)
            else: 
                result = helper(n-1) + helper(n-2)      
            cache[n] = result 
            return result 
            
        return helper(n)
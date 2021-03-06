class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        square = map(lambda x:x*x, nums)
        return sorted(square, reverse=False)
        

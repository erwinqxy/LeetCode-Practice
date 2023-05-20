class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def helper(l, r): 
            if l < r:
                s[l], s[r] = s[r], s[l]
                helper(l+1, r-1)
        helper(0, len(s)-1)
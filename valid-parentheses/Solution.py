class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Data structure to help solve 
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in brackets:
                top = stack.pop() if stack else None
                if brackets[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        def helper(root):
            if (root):
                helper(root.left)
                res = root.val
                inorder.append(res)
                helper(root.right) 
        helper(root)
        return inorder
    
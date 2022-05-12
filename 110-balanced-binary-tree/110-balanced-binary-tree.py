# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def depth(node):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            if abs(left - right) > 1:
                return False
            return 1 + max(left, right)
        
        return depth(root) and self.isBalanced(root.left) and self.isBalanced(root.right) 
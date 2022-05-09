# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_max = [0]
        
        def depth(node, cur_max):
            if not node:
                return 0
            
            left_depth = depth(node.left, cur_max)
            right_depth = depth(node.right, cur_max)
            cur_max[0] = max(cur_max[0], left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        depth(root, cur_max)
        return cur_max[0]
            
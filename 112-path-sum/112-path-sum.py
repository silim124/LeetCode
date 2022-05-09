# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        totals = []
        
        if not root:
            return False
        
        def dfs(node, total):
            if not node.left and not node.right:
                totals.append(total + node.val)
                print(totals)
                return
            total += node.val
            if node.left:
                dfs(node.left, total)
            if node.right:
                dfs(node.right, total)
        
        dfs(root, 0)
        if targetSum in totals:
            return True
        return False
            
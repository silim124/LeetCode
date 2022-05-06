"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        
        queue, clones = collections.deque([node]), {node.val: Node(node.val, [])}
        while queue:
            current = queue.popleft()
            current_clone = clones[current.val]
            
            for neighbor in current.neighbors:
                if not neighbor.val in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                current_clone.neighbors.append(clones[neighbor.val])
            
        return clones[node.val]
                    
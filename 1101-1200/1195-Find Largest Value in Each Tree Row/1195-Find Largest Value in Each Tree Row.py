"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        # write your code here
        if root is None:
            return []
        Q = [root]
        result = []
        while Q:
            result.append(max(node.val for node in Q))
            Q = [child for node in Q for child in (node.left, node.right) if child is not None]
        return result

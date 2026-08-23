# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def traverse(node, maxVal):
            if not node:
                return
            # print("node", node.val, "maxVal", maxVal)
            if node.val >= maxVal:
                maxVal = node.val
                self.ans += 1
            traverse(node.left, maxVal)
            traverse(node.right, maxVal)
        
        traverse(root, float("-inf"))
    
        return self.ans
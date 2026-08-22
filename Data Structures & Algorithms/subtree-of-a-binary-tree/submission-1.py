# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = []
        def findRoot(root, subRoot):
            if not root:
                return
            if root.val == subRoot.val:
                nodes.append(root)
            findRoot(root.left, subRoot)
            findRoot(root.right, subRoot)
        
        def compare(root, subRoot):
            if not root and not subRoot:
                return True            
            if root and not subRoot or not root and subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return compare(root.left, subRoot.left) and compare(root.right, subRoot.right)
        
        findRoot(root, subRoot)

        for node in nodes:
            # print("node", node.val)
            if compare(node, subRoot):
                return True
        return False
            
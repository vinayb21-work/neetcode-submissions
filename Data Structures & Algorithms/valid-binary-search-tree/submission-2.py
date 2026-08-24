# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []
        
        def inorderTraversal(root):
            if not root:
                return
            inorderTraversal(root.left)
            order.append(root.val)
            inorderTraversal(root.right)
        
        inorderTraversal(root)
        
        # print(order)

        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        
        return True
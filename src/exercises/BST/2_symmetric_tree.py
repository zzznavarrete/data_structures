"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Intuition: Check if the right leaf nodes, are equal of the left side of the tree
        
        def dfs(left:TreeNode, right:TreeNode) -> bool:
            # First, check if there are both leafs to compare
            if not left and not right:
                return True
            
            # In case there are one OR the other, it means that the tree is not symmetric.
            if not left or not right:
                return False
            
            
            # Check if the leafs accomplish the symmetric condition
            if left.val == right.val:
                # recursive call to check
                return (dfs(left.left, right.right) and
                       dfs(left.right, right.left))

        # Call to the recursive method
        return dfs(root.left, root.right)
        
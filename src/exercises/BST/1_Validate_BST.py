class Node:
    def __init__(self, value):
         self.value = value

class TreeNode:
    def __init__(self, value):
        self.root = Node(value)
        self.left = None
        self.right = None




class Solution:
    def isValidBST(self, root:TreeNode) -> bool:
        
        def valid(main: TreeNode, left: TreeNode, right: TreeNode) -> bool:
                if not main:
                    return True 
                
                if not (left < main.val< right):
                    return False
                
                return (valid(main.left, left, main.val) and valid(main.right, main.val, right))
            
        return valid(root, float('-inf'), float('inf'))
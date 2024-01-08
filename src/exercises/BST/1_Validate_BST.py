class Node:
    def __init__(self, value):
         self.value = value

class TreeNode:
    def __init__(self, value):
        self.root = Node(value)
        self.left = None
        self.right = None




class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Intuition: Validate if the childs notes, from the left side of the root are less than their current main root, and the other way around for the right side
        
        def valid(currentNode, left, right):
            # first, check if the current node exists
            if not currentNode:
                return True
            
            # Now the main, validation:
            if not (left < currentNode.val < right):
                return False
            
            # Now the recursion call
            # The first recursion call checks the boundaries for the left side of the tree, - 
            # - it makes sense to pass the right value as the current node because we need to check that the HL = the current value, 
            # - - since all the left leafs couldn't be greater than the current node, thus, our high limit.
            
            # For the right side of the tree, is similar, but we're checking that these leaf couldn't be lesser than the current value (thus, our Low Limit (LL))
            return (valid(currentNode.left, left, currentNode.val) and 
                    valid(currentNode.right, currentNode.val, right))
        
        
        # for initializing the algorithms, we pass the -inf and +inf as LL and HL of the tree node
        return valid(root, float('-inf'), float('inf'))
        
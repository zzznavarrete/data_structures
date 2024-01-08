"""
Given the root of a binary tree, 
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""


class Solution:
    
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check border case, empty tree
        if not root:
            return []
        
        # BFS Algorithm:
        def BFS(root: TreeNode) -> bool:
            """
            Perform the in-level population of a list to represent the tree values.
            """
            queue:list = []
            queue.append(root)
            result:list = []
                
            while len(queue) > 0:
                qLen:int = len(queue)
                subGroup:list = []
                    
                for _ in range(qLen):
                    currentNode = queue.pop(0)
                    
                    if currentNode:
                        subGroup.append(currentNode.val)
                        queue.append(currentNode.left)
                        queue.append(currentNode.right)
                        
                if subGroup:
                    result.append(subGroup)
                    
            return result
        
        return BFS(root)
    

""" 1st approach
    if not root:
        return []


    key:int = 0
    dictLevel:dict = {}


    dictLevel[key] = [root.val]

    def categorizeLevels(left, right, key:int) -> list:
        key += 1
        if not key in dictLevel.keys():
            dictLevel[key] = []

        if left:
            dictLevel[key].append(left.val)
            categorizeLevels(left.left,left.right, key=key)

        if right:
            dictLevel[key].append(right.val)
            categorizeLevels(right.left, right.right, key=key)


        return [value for (key,value) in dictLevel.items() if len(value) > 0]

    return categorizeLevels(root.left, root.right, key)

"""

    
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
    
    # 1st approach: (Myself)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
    
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



            

    # 2nd approach - Neetcode
    

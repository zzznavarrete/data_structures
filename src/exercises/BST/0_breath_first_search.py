
class Solution:

    def BFS(root) -> list:
        if not root:
            return []
        
        currentNode = root
        queue:list = []
        queue.append(currentNode)
        result:list = []

        while len(queue) > 0:
            currentNode = queue.pop(0)
            result.append(currentNode.value)

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)

        return result
    

 
    
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        """Insert a new value into an existent BST structure.

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        new_node = Node(value)

        # In case it's an empty tree
        if self.root is None:
            self.root = new_node 
            return True 
        
        temp = self.root

        while (True):
            if new_node.value == temp.value: # in case the value it's already there 
                return False
            if new_node.value < temp.value: # if the value is less than the evaluated node
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left 
            else: # if the value is more than the evaluated node 
                if temp.right is None:
                    temp.right = new_node
                    return True 
                temp = temp.right 

    

    def contains(self, value):
        """Verify the existant of a value in the tree. 

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        temp = self.root 
        while temp is not None:
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right 
            else:
                return True 
        
        return False 



if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree.insert(50)
    my_tree.insert(20)
    my_tree.insert(80)
    print(my_tree.root.value)
    print(my_tree.root.left.value)
    print(my_tree.root.right. value)

    print(my_tree.contains(20))
    print(my_tree.contains(22))
    my_tree.insert(22)
    print(my_tree.contains(22))
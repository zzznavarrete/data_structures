class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        """ 
        Method to append new nodes into a Linked List

        Args:
            value (node): New node tu append

        Returns:
            boolean: Determines if the method whas successful
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True


    def pop(self):
        """
        Deletes the last element an element of a Linked List.

        Returns:
            value of the new last node.
        """
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


    def prepend(self, value):
        """
        Append a new item at the beginning of the list.

        Args:
            value (any): value of the new node

        Returns:
            boolean: flag to notify the successfullness of the method.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True
    

    def pop_first(self):
        """
        Pops the first element of the linked list.

        Returns:
            Node: deleted node.
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

    def get(self, index):
        """Get the Node at the indicated index.

        Args:
            index (int): Required node position.

        Returns:
            Node: Asked node.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        

    def set_value(self, index, value):
        """Set specific value at specific node position.

        Args:
            index (int): Node position to set a value.
            value (int): Value to set.

        Returns:
            bool: Flag to notify the successfullness of the method.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

    def inset(self, index, value):
        """Insert a new item in a given position

        Args:
            index (_type_): _description_
            value (_type_): _description_

        Returns:
            bool: flag to notify the sucess.
        """
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        """Remove specific node

        Args:
            index (_type_): _description_

        Returns:
            _type_: _description_
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length == 1:
            return self.pop
        
        # this block is when I remove the node
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None

        self.length -= 1
        return temp
    

    def reverse(self):
        """
            Reverse the linked list all the way backwards.
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before # this line reverse the pointer
            before = temp
            temp = after




if __name__ == "__main__":
    # Creating a linked list
    my_linked_list = LinkedList(4)
    # Appending a new node
    my_linked_list.append(2)
    # Printing the entire list
    my_linked_list.print_list()

    # Poping to left 1 element
    print("*"*10)
    my_linked_list.pop()
    my_linked_list.print_list()

    # Poping to left with no element
    print("*"*10)
    my_linked_list.pop()
    my_linked_list.print_list()

    # pre appending new element
    print("*"*10)
    my_linked_list.append(1)
    my_linked_list.prepend(2)
    my_linked_list.print_list()

    # pre poping
    print("*"*10)
    my_linked_list.pop_first()
    my_linked_list.print_list()

    # Get method
    print("*"*10)
    my_linked_list.append(10)
    print(my_linked_list.get(1).value)


    # Set value
    print("*"*10)
    my_linked_list.set_value(1,20)
    my_linked_list.print_list()


    # Insert value at 1 position
    print("*"*10)
    my_linked_list.inset(1, 33)
    my_linked_list.print_list()

    # delting the node
    print("*"*10)
    my_linked_list.remove(1)
    my_linked_list.print_list()

    # reversing the list
    print("*"*10)
    my_linked_list.reverse()
    my_linked_list.print_list()

    


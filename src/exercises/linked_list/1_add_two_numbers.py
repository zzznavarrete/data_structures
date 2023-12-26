class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Returns a reversed linked list of the sum of the reversed representation of the inputs.
        """
        result_op:int = 0 #
        resultNode = cur = ListNode(0) # Initializing the node

        while l1 or l2 or result_op:
            if l1:
                result_op += l1.val
                l1 = l1.next 

            if l2:
                result_op += l2.val
                l2 = l2.next

            cur.next = ListNode(result_op % 10) # Storing the result up to 10 max
            cur = cur.next

            result_op //= 10

					
        return resultNode.next
        

if __name__ == "__main__":
    l1:ListNode = ListNode(3)
    l1.next = 4
    l1.next.next = 2
"""
You are given two non-empty linked lists representing two non-negative integers.
 The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1.- Check border cases: Empty linked lists, one of the two lists without nodes, etc
        if not l1 and not l2:
            return None
        
        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2

        

        # 2.- Perform the algorithm: a) reverse the linked list.
        # - c) Sum all the nodes in the reversed order (keep track of the results > 10 to pass the carry to the another node)
        # - d) reverse the linked list but the first element.
        reversedL1 = self.reverseLinkedList(l1)
        reversedL2 = self.reverseLinkedList(l2)


        resList = curr = ListNode(0)
        carry:int = 0
        # Now I need to iterate over the
        while reversedL1 or reversedL2 or carry:
            if reversedL1:
                carry += reversedL1.val
                reversedL1 = reversedL1.next
            
            if reversedL2:
                carry += reversedL2.val
                reversedL2 = reversedL2.next

            curr.next = ListNode(carry % 10)
            curr = curr.next

            carry //= 10

        return self.reverseLinkedList(resList.next)


         



    def reverseLinkedList(self, head:ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
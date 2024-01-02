# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        i:int = 1
        
        tmp = None
        while head:
            tmp = self.reverseLinkedList(head=head)
            break

        return tmp



    def reverseLinkedList(self, head:ListNode) -> ListNode:
        prev, curr = None, head
        i = 0
        while curr:
            if i == 2:
                break
            nxt = curr.next
            curr.next = prev
            prev = curr
            
            curr = nxt
            i += 1
        
        nxt = prev.next
        if curr:
            nxt.next = self.reverseLinkedList(curr)  # 2nd node of the 2nd group
        prev.next = nxt

        return prev 

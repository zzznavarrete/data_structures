class ListNode:

    def __init__(self, val:int = 0, next = None, random = None):
        self.val = val
        self.next = next 
        self.random = random


class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        oldToNew:dict = {None:None}
        cur = head 
        while cur:
            temp = ListNode(x=cur.val)
            oldToNew[cur] = temp
            cur = cur.next 

        cur = head 
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next 
        

        return oldToNew[cur]

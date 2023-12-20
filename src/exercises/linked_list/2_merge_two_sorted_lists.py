class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 or list2:
            # Need to check if have value 
            
            if list1 and list2:
                # Main logic    
                if list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    cur = cur.next
                    list1 = list1.next
                else:
                    cur.next = ListNode(list2.val)
                    cur = cur.next
                    list2 = list2.next

            elif not list1 and list2:
                # Program to if not more l1 node
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
            elif not list2 and list1:
                # program to if not more l2 node
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next

            
        return dummy.next

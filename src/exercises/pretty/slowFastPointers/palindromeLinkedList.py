# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Border case:
        if not head:
            return False 
            
        # Two pointers  (slow and fast) approach

        # 1st, find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        
        # Now when the previous loop breaks, the 'slow' pointer will be at the middle of the linked list
        # - then, now we need to reverse it

        revSlow = self.reverseLinkedList(slow)


        # Now, I need to compare both lists (the middle-reversed one) and the original, if it is a palindrome,
        # - then both values will be the same until the middle cutted reversed list reach to its end.

        return self.compareLinkedLists(head, revSlow)


    def compareLinkedLists(self, firstList, secondList) -> bool:
        if not firstList or not secondList:
            return False

        while firstList and secondList:
            if firstList.val == secondList.val:
                firstList = firstList.next
                secondList = secondList.next
            else:
                return False

        return True

    def reverseLinkedList(self, head) -> ListNode:
        if not head:
            return None

        prev, curr = None, head

        while curr:
            nxt = curr.next 

            curr.next = prev 
            prev = curr 

            curr = nxt 

        return prev 
    




if __name__ == "__main__":
    nodeList = ListNode(1)
    nodeList.next = ListNode(2)
    nodeList.next = ListNode(3)
    nodeList.next = ListNode(2)
    nodeList.next = ListNode(1)


    sol = Solution()

    print(sol.isPalindrome(nodeList))



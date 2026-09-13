# Session 1, attempt 3: after watching video
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        # second is now the beginning of second half of the list
        
        prev = None
        while second: # reversing here
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merging the two lists
        norm, rev = head, prev 

        while rev: # because rev, the second half, is the smaller or equal half
            tmp1, tmp2 = norm.next, rev.next
            norm.next = rev
            rev.next = tmp1

            norm = tmp1
            rev = tmp2





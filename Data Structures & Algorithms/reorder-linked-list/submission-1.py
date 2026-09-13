# Session 1, Attempt 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hold = head

        while hold: 
            if not hold.next:
                break 

            scout = hold.next
            prev = hold

            while scout.next:
                scout = scout.next
                prev = prev.next

            prev.next = None
            scout.next = hold.next
            hold.next = scout
            hold = hold.next.next
        



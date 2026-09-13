# Session 2, attempt 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: 
            return False
        
        slow, fast = head, head

        while fast:
            if fast.next is None:
                return False

            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
                

            
        return False
            
        
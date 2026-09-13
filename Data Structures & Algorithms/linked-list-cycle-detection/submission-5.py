# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not (head and head.next):
            return False
        slow = head
        fast = head.next.next

        while slow and fast:
            if slow == fast: #WE ARE GOOD HERE BUT KEEP IN MIND THAT NONE TYPE CAN"T BE COMPARED WITH ==. ONLY IS AND IS NOT.
                return True
            else:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    return False
        
        return False
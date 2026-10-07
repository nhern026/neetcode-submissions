# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1

        curr = head
        while curr:
            curr = curr.next
            length += 1

        # z[a, b, c, d, e, f].   6-5 = 1
        # print(length - n)
        dummyHead = ListNode(next=head)
        curr = dummyHead
        for _ in range(length - n - 1):
            curr = curr.next

        curr.next = curr.next.next
        
        return dummyHead.next


        
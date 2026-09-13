# Session 2, attempt 2. read goodpoint from last attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        curr = dummy

#changed from goodpoint in last attempt: for next time, it could be even better, think how??
        while list1 or list2:
            if list1 and not list2:
                curr.next = list1 
                break # change
            elif list2 and not list1: 
                curr.next = list2
                break # change
            elif list2.val <= list1.val: #both lists exist but list2 is smaller or equals
                curr.next = list2
                list2 = list2.next
            else: #list1 is smaller
                curr.next = list1 
                list1 = list1.next
            curr = curr.next
            
        return dummy.next
        
                
            
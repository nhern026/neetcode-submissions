# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        curr = dummy
        prev = None

        while list1 or list2:
            if list1 and not list2: #only list1 exists
                curr.next = list1 # logic here for adding to end of list
                list1 = list1.next # logic for moving forward
            elif list2 and not list1: 
                curr.next = list2
                list2 = list2.next
            elif list2.val <= list1.val: #both lists exist but list2 is smaller or equals
                curr.next = list2
                list2 = list2.next
            else: #list1 is smaller
                curr.next = list1 
                list1 = list1.next
            curr = curr.next
            
        return dummy.next
        
                
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        blue, red = list1, list2
        newHead = None
        prev = None

        while blue or red:
            # comapring the lists


            if blue and red: #if both pointers are not None
                if blue.val < red.val:
                    if prev: 
                        prev.next = blue
                    else:
                        newHead = blue
                    prev = blue
                    blue = blue.next
                else:
                    if prev:
                        prev.next = red
                    else:
                        newHead = red
                    prev = red
                    red = red.next
            elif blue: #if its just blue
                if prev: 
                    prev.next = blue
                else:
                    newHead = blue
                prev = blue
                blue = blue.next

            elif red: # if its just red
                if prev:
                    prev.next = red
                else:
                    newHead = red
                prev = red
                red = red.next
        

        return newHead


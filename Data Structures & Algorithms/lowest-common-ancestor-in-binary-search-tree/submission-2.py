# Session 1, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# okay so basically my code uses a helper function to save our p's ancestry list and our q's ancestry list
# once you have those two saved, then you start working backwards to see what they have in common

import copy

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.pSeenList = []
        self.qSeenList = []

        def buildAncestorList(curr, seenList, p, q):
            if self.pSeenList and self.qSeenList:
                return
            if not curr:
                return

            seenList.append(curr)

            if curr is p:
                self.pSeenList = copy.deepcopy(seenList)
            elif curr is q:
                self.qSeenList = copy.deepcopy(seenList)
            
            buildAncestorList(curr.left, seenList, p, q)
            buildAncestorList(curr.right, seenList, p, q)

            x = seenList.pop()
            return
        
        buildAncestorList(root, [], p, q)

        if len(self.pSeenList) < len(self.qSeenList):
            shorter = self.pSeenList
            longer = self.qSeenList
        else:
            longer = self.pSeenList
            shorter = self.qSeenList

        #changed this so we don't have to 
        for shortID in range(len(shorter)-1, -1, -1): 
            longID = shortID

            if shorter[shortID].val == longer[longID].val:
                return shorter[shortID]

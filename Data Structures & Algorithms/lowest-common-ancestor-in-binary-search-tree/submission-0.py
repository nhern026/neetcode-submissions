# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

        #my lists work!
        # for x in self.pSeenList:
        #     print(x.val, end=" ")
        # print()
        # for y in self.qSeenList:
        #     print(y.val, end=" ")
        

        if len(self.pSeenList) < len(self.qSeenList):
            shorter = self.pSeenList
            longer = self.qSeenList
        else:
            longer = self.pSeenList
            shorter = self.qSeenList


        for x in shorter:
            print(x.val, end=" ")
        print()
        for y in longer:
            print(y.val, end=" ")
        
        print("")

        shortID = len(shorter) - 1
        for longID in range(len(longer)-1, -1, -1):
            if longID < len(shorter):
                shortID = longID
            print(shorter[shortID].val, longer[longID].val)

            if shorter[shortID].val == longer[longID].val:
                return shorter[shortID]

        return "HEY"

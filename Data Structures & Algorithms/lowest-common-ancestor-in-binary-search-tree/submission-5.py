# Session 1, attempt 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# okay all i changed was how we worked backwards in the last sequence. 

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.pSeenList = []
        self.qSeenList = []

        def buildAncestorList(curr, seenList, p, q):
            if not curr:
                return              
            if self.pSeenList and self.qSeenList:
                return

            seenList.append(curr)

            if curr is p:
                self.pSeenList = seenList.copy() # deepcopy would also make new tree nodes in there, but we really only care about preserving the list order and size.
            elif curr is q:
                self.qSeenList = seenList.copy()
            
            buildAncestorList(curr.left, seenList, p, q)
            buildAncestorList(curr.right, seenList, p, q)

            x = seenList.pop()
            return
        
        # O(n) because it goes through all of tree
        buildAncestorList(root, [], p, q)

        # changed this so we don't have to worry about updating shortID in such a weird way.
        # O(h) where h is height
        min_length = min(len(self.pSeenList), len(self.qSeenList)) 

        for id in range(min_length-1, -1, -1): 

            if self.pSeenList[id] is self.qSeenList[id]:
                return self.pSeenList[id]

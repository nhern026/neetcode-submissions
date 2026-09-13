# Session 1, attempt 2: after reading hint 1 and thenw watching gid

# this attempt is Breadth First Search (BFS)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        goingToVisit = queue.Queue()
        goingToVisit.put(root)

        while goingToVisit.qsize() > 0:
            lvlList = []
            for _ in range(goingToVisit.qsize()):
                curr = goingToVisit.get()
                lvlList.append(curr.val)
                if curr.left:
                    goingToVisit.put(curr.left)
                if curr.right:
                    goingToVisit.put(curr.right)
            res.append(lvlList)

        return res
            
            






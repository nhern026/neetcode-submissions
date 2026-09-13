# Session 2, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque as dq

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # store vals in the list, not the actual node

        if not root:
            return []

        queue = dq()
        queue.append(root)

        res = []

        while queue:
            levelList = []
            queueLength = len(queue)

            for _ in range(queueLength):
                curr = queue.popleft()
                levelList.append(curr.val)
                
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(levelList)
    
        return res


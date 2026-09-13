# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = defaultdict(list)

        def traverse(curr, depth):
            if not curr:
                return

            self.levels[depth].append(curr.val)
            traverse(curr.left, depth+1)
            traverse(curr.right, depth+1)
        
        traverse(root, 0)

        return list(self.levels.values())


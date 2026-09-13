#Chat's answer in reference to mine. take note how it doesn't compare in the firs method, becuase you already do that in the helper function! much cleaner
class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:

        def sameTree(A, B):
            if A is None and B is None:
                return True

            if A is None or B is None or A.val != B.val:
                return False

            return (
                sameTree(A.left, B.left)
                and sameTree(A.right, B.right)
            )

        def search(curr):
            if curr is None:
                return False

            if sameTree(curr, subRoot):
                return True

            return search(curr.left) or search(curr.right)

        return search(root)
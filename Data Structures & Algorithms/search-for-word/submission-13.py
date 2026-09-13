# Session 1, atttempt 1
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighb_transformations = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()

        def dfs(r, c, i): # use i as comparison, assume everything else behind is good because it is!
            if not (0 <= r < len(board) and 0<= c < len(board[0])):
                return False
            if (r, c) in seen:
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            seen.add((r,c))
            
            for transform in neighb_transformations:
                new_r = r + transform[0]
                new_c = c + transform[1]

                if dfs(new_r, new_c, i+1):
                    return True
                    
            seen.remove((r, c))
            return False


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False
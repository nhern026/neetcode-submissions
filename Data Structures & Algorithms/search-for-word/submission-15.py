# Session 3, attempt 1
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        board = 
       [["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]],
    
        dfs(r, c, i): #board[r][c] is a letter on the graph
            if i == len(word):
                return True
            if r and c not valid: 
                return False
            if board[r][c] ==  word[i]:
                for each edge:
                    if that new dfs is true:
                        return true

            return False

        L == |word|, 3^L for backtracking dfs
        time: O(n x m * (3^L)), for each letter in graph, run backtracking dfs
        space: O(L) <-- recursive stack and visited set
        """
        ROWS, COLS = len(board), len(board[0])
        TRANSFORMS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r,c) in visited:
                return False
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return False
            
            visited.add((r,c))
            if board[r][c] == word[i]:
                for t in TRANSFORMS:
                    new_r = r + t[0]
                    new_c = c + t[1]
                    if dfs(new_r, new_c, i+1):
                        return True
            visited.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                if dfs(r, c, 0):
                    return True

        return False
        



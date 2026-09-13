# Session 1, attempt 3. With chat fix of passing index. otherwise slicing would make new string each time.
# ... good to know

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [(-1, 0), (0, -1), (1, 0), (0,1)]

        def search(seen, i, j, word_idx):
            print(word_idx)
            if board[i][j] != word[word_idx]:
                return False
            if word_idx == len(word) - 1: 
                return True
            
            seen.add((i, j))

            for transform in neighbors:
                new_i = i + transform[0]
                new_j = j + transform[1]

                if not((new_i, new_j) in seen):
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                        if search(seen, new_i, new_j, word_idx+1):
                            return True

            seen.remove((i, j))
            return False

    
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if search(seen, i, j, 0):
                    return True

        return False
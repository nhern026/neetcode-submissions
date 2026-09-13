# Session 1, attempt 2
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [(-1, 0), (0, -1), (1, 0), (0,1)]
        # up, left, down, right


        def search(seen, palabra, i, j):

            if board[i][j] != palabra[0]:
                return False
            # at this point our letter corresponds to the curr ltr in word
            if len(palabra) == 1: #base case, we found last letter
                return True
            
            seen.add((i, j))

            for transform in neighbors:
                new_i = i + transform[0]
                new_j = j + transform[1]

                # asking here if neighbor is not visited before and within board bounds
                if not((new_i, new_j) in seen):
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                        if search(seen, palabra[1:], new_i, new_j):
                            return True

                # issue: we can't update seen like this, we are going to lose possible solutions!
            seen.remove((i, j))
            return False

    
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if search(seen, word, i, j):
                    return True

        return False



# is the board always rectangle --> yes
# is the board always non emtpy --> yes
# are there some spots in the board that are None?  --> yes
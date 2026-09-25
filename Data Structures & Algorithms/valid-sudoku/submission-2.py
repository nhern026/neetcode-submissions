class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        checkerSet = set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                else:
                    num = int(board[r][c])
                    if num in checkerSet:
                        return False
                    else:
                        checkerSet.add(num)
            checkerSet = set()
        
        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                else:
                    num = int(board[r][c])
                    if num in checkerSet:
                        return False
                    else:
                        checkerSet.add(num)
            checkerSet = set()
        
        for starting_r in range(0, 9, 3):
            for starting_c in range(0, 9, 3):
                for r in range(starting_r, starting_r + 3):
                    for c in range(starting_c, starting_c + 3):
                        if board[r][c] == ".":
                            continue
                        else:
                            num = int(board[r][c])
                            if num in checkerSet:
                                return False
                            checkerSet.add(num)

                checkerSet = set()

        return True
        

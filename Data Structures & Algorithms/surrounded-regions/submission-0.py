class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #perform dfs on the edges where the cell is "O"
        ROWS, COLS = len(board), len(board[0])
        NEIGHBOR_TRANS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        oSet = set()


        def findO(r, c): #dfs to find all O's
            # if we're out of the board, return
            # if we're already in the visit set, return
            # if we're not O, return
            if not (0 <= r < ROWS and 0 <= c < COLS) or ((r, c) in oSet) or (board[r][c] != 'O'):
                return

            #otherwise --> add to set, add children/neighbors to set
            else:     
                oSet.add((r,c))
                for trans in NEIGHBOR_TRANS:
                    findO(r + trans[0], c + trans[1])



        # find where all O regions touch the edges:
        for r in range(ROWS): #first and last column
            findO(r, 0)
            findO(r, COLS-1)
        for c in range(COLS): #first and last row
            findO(0, c)
            findO(ROWS-1, c)

        # turn all other O regions into X's

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in oSet:
                    board[r][c] = 'X'
        


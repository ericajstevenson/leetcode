# use a hash set to look for duplicates in each row, column, and square (same as dictionary)
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # hash set for the columns (key is col #, value is a set)
        rows = collections.defaultdict(set) # hash set for the rows
        squares = collections.defaultdict(set) # hash set for the squares (key = (row/3, c/3))

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or # if the value is already in the hash set for rows or cols
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3,c // 3]):
                    return False

                # update hash sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3,c // 3].add(board[r][c])
        return True






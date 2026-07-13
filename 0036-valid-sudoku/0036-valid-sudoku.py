class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_board = []
        for i in range (9):
            col_board.append([sublist[i] for sublist in board])
        
        def get_square(board, square_num):
            sr = (square_num // 3) * 3
            sc = (square_num % 3) * 3
            return [
                board[sr][sc], board[sr][sc + 1], board[sr][sc + 2],
                board[sr + 1][sc], board[sr + 1][sc + 1], board[sr + 1][sc + 2],
                board[sr + 2][sc], board[sr + 2][sc + 1], board[sr + 2][sc + 2],
            ]
        
        all_squares = [get_square(board, i) for i in range(9)]
        
        for row in board + col_board + all_squares:
            row = [x for x in row if x != "."]
            if len(row) != len(list(set(row))):
                return False
        return True
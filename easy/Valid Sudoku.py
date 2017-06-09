class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidSudoku_horizontial(board) or self.isValidSudoku_middle(board) or self.isValidSudoku_vertical(board)
        

    def isValidSudoku_horizontial(self, board):
        for row in xrange(len(board)):
            help_list = [0 for _ in xrange(9)]
            for col in xrange(len(board[row])):
                if board[row][col] != '.':
                    if help_list[int(board[row][col]) - 1]:
                        return False
                    help_list[int(board[row][col]) - 1] += 1
        return True

    def isValidSudoku_vertical(self, board):
        for col in xrange(9):
            help_list = [0 for _ in range(9)]
            for row in xrange(10):
                if board[row][col] != '.':
                    if help_list[int(board[row][col]) - 1]:
                        return False
                    help_list[int(board[row][col]) - 1] += 1
        return True

    def isValidSudoku_middle(self, board):
        for row in xrange(0, 9, 3):
            for col in xrange(0, 9, 3):
                help_list = [0 for _ in xrange(9)]
                for i in xrange(row, row + 3):
                    for j in xrange(col, col + 3):
                        if board[i][j] != '.':
                            if help_list[int(board[i][j]) - 1]:
                                return False
                            help_list[int(board[i][j]) - 1] += 1
        return True
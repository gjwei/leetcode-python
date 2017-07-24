class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        [r, c] = click
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
            return
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return
        elif board[r][c] == 'E':
            _count_adjacent_mines = self.count_adjacent_mines(board, r, c)
            if _count_adjacent_mines == 0:
                board[r][c] = 'B'
                if r - 1>= 0:
                    self.updateBoard(board, [r - 1, c])
                if r + 1 < len(board):
                    self.updateBoard(board, [r + 1, c])
                if c - 1 >= 0:
                    self.updateBoard(board, [r, c - 1])
                if  c + 1 < len(board[r]):
                    self.updateBoard(board, [r, c + 1])
                return
            else:
                board[r][c] = str(_count_adjacent_mines)
                return
        
        
    def count_adjacent_mines(self, board, x, y):
        result = 0 
        for i in xrange(x - 1, x + 2):
            for j in xrange( y - 1, y + 2):
                if 0 <= i < len(board) and 0 <= j < len(board[i]):
                    result += (board[i][j] == 'M')
        return result
                
s = Solution()
a = ["EEEEEEEE","EEEEEEEM","EEMEEEEE","MEEEEEEE","EEEEEEEE","EEEEEEEE","EEEEEEEE","EEMMEEEE"]
for i in range(len(a)):
    a[i] = list(a[i])
    print a[i]

print s.count_adjacent_mines(a, 2, 1)
s.updateBoard(a, [0, 0])
print ''
for i in a:
    print i
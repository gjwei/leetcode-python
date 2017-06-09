class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] == 1:
                    result += self.caculate_perimeter(grid, x, y)
        return result
                
    def caculate_perimeter(self, grid, x, y):
        top, bottom, left, right = 0, 0, 0, 0
        if x == 0 or grid[x - 1][y] == 0:
            top = 1
        if x == len(grid) - 1 or grid[x + 1][y] == 0:
            bottom = 1
        if y == 0 or grid[x][y - 1] == 0:
            left == 1
        if y == len(grid[0]) - 1 or grid[x][y + 1] == 0:
            right = 1
        return (top + bottom + left + right)
        

            
        


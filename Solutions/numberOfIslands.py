class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '0':
                    self.dfs(grid,i,j)
                    num += 1
                    
        return num
    
    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        


def main():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
            
    ret = Solution().numIslands(grid)

    print ret


if __name__ == '__main__':
    main()
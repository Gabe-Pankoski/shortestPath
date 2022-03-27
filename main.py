def minPathSum(grid: list[list[int]]) -> int:
    height = len(grid)-1
    width = len(grid[0])-1
    #If input is a single value
    if width == 0 and height == 0:
            return grid[0][0]
    #If input is a row vector
    elif width == 0 and height != 0:
        minValue = 0
        for i in range(height, -1, -1):
            minValue += grid[i][0]
        return abs(minValue)
    #If input is a column vector
    elif height == 0 and width != 0:
        minValue = 0
        for i in range(width, -1, -1):
            minValue += grid[0][i]
        return abs(minValue)
    #Regular input
    else:
        #Bottom Row
        for i in range(width-1, -1, -1):
            grid[height][i] += grid[height][i+1]
        #Far Right Column
        for i in range(height-1, -1, -1):
            grid[i][width] += grid[i+1][width]
        #Begin traversing rest of matrix
        #Right to left
        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                val = min(grid[i+1][j], grid[i][j+1])
                grid[i][j] += val
        return abs(grid[0][0])
    


#path = [ [1, 3, 3], [ 4, 9, 7 ], [ 1, 1, 3] ]
path = [[1,3,1],[1,5,1],[4,2,1]]
out = minPathSum(path)
print(out)


#print(validMove((1,2), 3, 3))
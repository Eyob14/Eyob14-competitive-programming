def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    rows = len(board)
    cols = len(board[0])
    def dfs(board, row, col, visited):
        position = (row, col)
        if not(0<=row<rows) or not(0<=col<cols):
            return False
        if position in visited:
            return False
        visited.add(position)
        if board[row][col] == 'O':
            board[row][col] = 'Y'                    
            dfs(board, row - 1, col, visited)
            dfs(board, row + 1, col, visited)
            dfs(board, row, col - 1, visited)
            dfs(board, row, col + 1, visited)
        # return True
            
    visited = set()
    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                dfs(board, row, col, visited) 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'Y':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","X","X"],
         ["X","O","o","X"]]
# board = [["X"]]
solve(board)
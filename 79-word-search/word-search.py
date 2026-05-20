class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c, index):
            # Base Case 1: If we matched all characters successfully
            if index == len(word):
                return True
                
            # Base Case 2: Out of bounds or current cell doesn't match target character
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[index]):
                return False
            
            # Step 3: Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Step 4: Explore all 4 adjacent directions
            # (Down, Up, Right, Left)
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Step 5: Backtrack - restore the original character
            board[r][c] = temp
            
            return found

        # Traverse every cell in the grid to find a potential starting point
        for r in range(ROWS):
            for c in range(COLS):
                # Optimize: Only start DFS if the first character matches
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False
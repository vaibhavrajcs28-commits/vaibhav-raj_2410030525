class Solution:
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
            
        ans = []
        n = len(mat)     # Number of rows
        m = len(mat[0])  # Number of columns
        
        # Initialize the 4 boundary pointers
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse Right along the top row
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1
            
            # 2. Traverse Down along the right column
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1
            
            # 3. Traverse Left along the bottom row (if rows remain)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1
                
            # 4. Traverse Up along the left column (if columns remain)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1
                
        return ans
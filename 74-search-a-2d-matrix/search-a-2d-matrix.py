class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        
        # Define search boundaries for the virtual 1D array
        low = 0
        high = (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Map the 1D index 'mid' to 2D matrix coordinates
            row = mid // n
            col = mid % n
            
            mid_element = matrix[row][col]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1  # Search the right half
            else:
                high = mid - 1 # Search the left half
                
        return False
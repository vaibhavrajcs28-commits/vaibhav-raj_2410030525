from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Total elements and the target count required to find the median position
        total_elements = n * m
        required_count = total_elements // 2
        
        # Step 1: Find the absolute minimum and maximum element in the matrix
        low = min(mat[i][0] for i in range(n))
        high = max(mat[i][-1] for i in range(n))
        
        ans = low
        
        # Step 2: Binary Search on the value range
        while low <= high:
            mid = (low + high) // 2
            
            # Count elements less than or equal to 'mid' across all rows
            count = 0
            for i in range(n):
                count += bisect_right(mat[i], mid)
                
            # Step 3: Shrink search space based on the count
            if count <= required_count:
                low = mid + 1
            else:
                ans = mid  # mid could be a potential median candidate
                high = mid - 1
                
        return ans
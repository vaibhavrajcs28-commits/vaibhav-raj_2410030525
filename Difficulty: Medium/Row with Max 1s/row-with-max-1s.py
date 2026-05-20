class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        if m == 0:
            return -1
            
        # Start at the top-right corner
        row = 0
        col = m - 1
        max_row_idx = -1
        
        while row < n and col >= 0:
            if arr[row][col] == 1:
                # We found a '1'. This row is a candidate for max 1s.
                max_row_idx = row
                # Move left to see if there are more 1s in this row
                col -= 1
            else:
                # We hit a '0'. No point looking left in this row.
                # Move down to check the next row.
                row += 1
                
        return max_row_idx
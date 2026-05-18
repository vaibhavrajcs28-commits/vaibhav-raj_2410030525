class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If the array has only 1 element, we are already at the end
        if n <= 1:
            return 0
            
        # If the first element is 0, we can't move anywhere
        if arr[0] == 0:
            return -1
            
        max_reach = arr[0]
        step_end = arr[0]
        jumps = 1
        
        # Start traversing from index 1 to n-1
        for i in range(1, n):
            # If we've reached the last element, return the total jumps
            if i == n - 1:
                return jumps
                
            # Update the maximum reach possible from the current position
            max_reach = max(max_reach, i + arr[i])
            
            # If we reach the end of the current jump's range
            if i == step_end:
                jumps += 1      # We must make another jump
                step_end = max_reach  # Update the boundary to our furthest reach
                
                # If the boundary cannot progress further and we haven't reached the end
                if i >= max_reach:
                    return -1
                    
        return -1
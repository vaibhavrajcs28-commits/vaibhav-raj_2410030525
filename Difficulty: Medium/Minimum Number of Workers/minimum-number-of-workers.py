class Solution:
    def minMen(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # Step 1: Collect all valid intervals
        intervals = []
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))
                
        if not intervals:
            return -1
            
        # Step 2: Sort intervals primarily by start time
        intervals.sort()
        
        workers = 0
        current_farthest = -1 # Tracks maximum reached position
        i = 0
        num_intervals = len(intervals)
        
        # We need to cover from position 0 up to n - 1
        while current_farthest < n - 1:
            # Find the next starting boundary we need to connect with
            # Initially we need something starting at 0 (<= current_farthest + 1)
            next_start_limit = current_farthest + 1
            best_reach = current_farthest
            
            # Check all intervals that can cover or connect to the next segment
            while i < num_intervals and intervals[i][0] <= next_start_limit:
                best_reach = max(best_reach, intervals[i][1])
                i += 1
                
            # If we could not advance our reach, there's a gap we can't cross
            if best_reach == current_farthest:
                return -1
                
            # Commit to the best worker interval found
            workers += 1
            current_farthest = best_reach
            
        return workers
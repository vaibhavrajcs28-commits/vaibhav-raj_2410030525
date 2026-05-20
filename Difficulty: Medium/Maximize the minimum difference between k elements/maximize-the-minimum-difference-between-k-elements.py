class Solution:
    def maxMinDiff(self, arr, k):
        # Step 1: Sort the array to check greedy placement easily
        arr.sort()
        n = len(arr)
        
        # Helper function to check if we can place 'k' elements with at least 'mid_diff' gap
        def is_feasible(mid_diff):
            count = 1  # Greedily place the first element
            last_placed = arr[0]
            
            for i in range(1, n):
                if arr[i] - last_placed >= mid_diff:
                    count += 1
                    last_placed = arr[i]
                    # If we successfully placed all k elements, this gap is valid
                    if count >= k:
                        return True
            return False

        # Step 2: Binary Search over the possible difference range
        low = 1
        high = arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_feasible(mid):
                ans = mid       # 'mid' is valid, record it as a candidate answer
                low = mid + 1   # Try to find a larger maximum-minimum gap
            else:
                high = mid - 1  # 'mid' is too large, look for a smaller gap
                
        return ans
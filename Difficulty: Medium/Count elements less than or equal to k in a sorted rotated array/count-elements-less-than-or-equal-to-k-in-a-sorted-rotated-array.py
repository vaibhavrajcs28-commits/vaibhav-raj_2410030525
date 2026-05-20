from bisect import bisect_right

class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        if n == 0:
            return 0
            
        # Step 1: Find the pivot index (index of the minimum element)
        low = 0
        high = n - 1
        pivot = 0
        
        while low <= high:
            # If the current window is already sorted, arr[low] is the minimum
            if arr[low] <= arr[high]:
                pivot = low
                break
                
            mid = (low + high) // 2
            next_idx = (mid + 1) % n
            prev_idx = (mid - 1 + n) % n
            
            # Check if mid element is the minimum element
            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                pivot = mid
                break
            
            # Decide which half to discard
            if arr[mid] >= arr[low]:
                # Left half is sorted, minimum lies in the right half
                low = mid + 1
            else:
                # Right half is sorted, minimum lies in the left half
                high = mid - 1
                
        # Step 2: Split into two sorted subarrays based on the pivot
        left_part = arr[0:pivot]
        right_part = arr[pivot:n]
        
        # Step 3: Count elements <= x in both parts using binary search
        count_left = bisect_right(left_part, x)
        count_right = bisect_right(right_part, x)
        
        return count_left + count_right
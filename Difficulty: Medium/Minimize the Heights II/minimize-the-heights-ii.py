class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        if n == 1:
            return 0
            
        # Step 1: Sort the array
        arr.sort()
        
        # Initial difference between max and min
        ans = arr[-1] - arr[0]
        
        # Step 2: Traverse the array to find the minimum possible maximum-difference
        for i in range(n - 1):
            # If subtracting k results in a negative height, it's invalid
            if arr[i+1] - k < 0:
                continue
                
            # Find the new potential minimum and maximum elements
            min_elem = min(arr[0] + k, arr[i+1] - k)
            max_elem = max(arr[-1] - k, arr[i] + k)
            
            # Update the answer with the minimum range found so far
            ans = min(ans, max_elem - min_elem)
            
        return ans
        
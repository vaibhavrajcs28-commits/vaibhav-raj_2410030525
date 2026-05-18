class Solution:
    def maxWater(self, arr):
        if not arr:
            return 0
            
        left = 0
        right = len(arr) - 1
        
        left_max = 0
        right_max = 0
        
        total_water = 0
        
        while left <= right:
            # The smaller maximum wall dictates how much water can be trapped
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]  # Update highest wall to the left
                else:
                    total_water += left_max - arr[left]  # Water trapped above current block
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]  # Update highest wall to the right
                else:
                    total_water += right_max - arr[right]  # Water trapped above current block
                right -= 1
                
        return total_water
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # If target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Step 1: Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target falls within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Shrink to left half
                else:
                    low = mid + 1   # Explore right half
                    
            # Step 2: Otherwise, the right half must be sorted
            else:
                # Check if target falls within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Shrink to right half
                else:
                    high = mid - 1  # Explore left half
                    
        # Target was not found in the array
        return -1
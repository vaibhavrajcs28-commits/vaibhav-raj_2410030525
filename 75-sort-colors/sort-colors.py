class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap and move BOTH low and mid forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in the right place, just move mid forward
                mid += 1
            else: # nums[mid] == 2
                # Swap with high, decrement high BUT DO NOT increment mid
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
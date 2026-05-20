class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        n = len(nums)
        
        # Base check
        if n < 4:
            return quadruplets
            
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Fix the first element
        for i in range(n - 3):
            # Skip duplicate values for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Fix the second element
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Step 4: Two-pointer approach for the remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for the third position
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate values for the fourth position
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        # Move both pointers inward after finding a match
                        left += 1
                        right -= 1
                        
                    elif current_sum < target:
                        left += 1 # We need a larger sum
                    else:
                        right -= 1 # We need a smaller sum
                        
        return quadruplets
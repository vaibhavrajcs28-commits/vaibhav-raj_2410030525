class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the array has only 1 element, we are already at the destination
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Iterate up to len(nums) - 2 because once we reach or cross 
        # the last index, no further jumps need to be evaluated.
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from the current position
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump range
            if i == current_end:
                jumps += 1            # Increment the jump counter
                current_end = farthest # Update the boundary for the next jump level
                
                # Optimization: If the next range already reaches or exceeds 
                # the destination, we can break early.
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps
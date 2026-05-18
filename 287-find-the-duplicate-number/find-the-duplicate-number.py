class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize tortoise and hare
        # Both start at the first position
        tortoise = nums[0]
        hare = nums[0]
        
        # Step 2: Find the intersection point inside the cycle
        while True:
            tortoise = nums[tortoise]        # Moves 1 step
            hare = nums[nums[hare]]          # Moves 2 steps
            if tortoise == hare:
                break
                
        # Step 3: Find the entrance to the cycle (the duplicate number)
        # Move tortoise back to the start, leave hare at the intersection
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]        # Both move at the same speed now
            hare = nums[hare]
            
        return tortoise
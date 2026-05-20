class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the list in reverse order (right to left)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # Early return since no more carries are possible
            
            # If the digit is 9, it becomes 0 and carry moves left
            digits[i] = 0
            
        # If we exit the loop, it means all digits were 9 (e.g., [9, 9] -> [0, 0])
        # We need to prepend a 1 at the beginning
        return [1] + digits
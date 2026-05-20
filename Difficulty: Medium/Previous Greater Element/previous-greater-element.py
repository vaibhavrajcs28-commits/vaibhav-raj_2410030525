class Solution:
    def preGreaterEle(self, arr):
        result = []
        stack = []
        
        for num in arr:
            # Maintain monotonic decreasing property:
            # Remove elements from stack that are less than or equal to the current number
            while stack and stack[-1] <= num:
                stack.pop()
                
            # If stack is empty, no greater element exists on the left
            if not stack:
                result.append(-1)
            else:
                # Top of the stack is the nearest strictly greater element to the left
                result.append(stack[-1])
                
            # Push current element onto the stack
            stack.append(num)
            
        return result
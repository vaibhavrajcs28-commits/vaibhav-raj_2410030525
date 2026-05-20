class Solution:
    def prevSmaller(self, arr):
        result = []
        stack = []
        
        for num in arr:
            # Maintain monotonic increasing property: 
            # Remove all elements from the stack that are greater than or equal to 'num'
            while stack and stack[-1] >= num:
                stack.pop()
            
            # If stack is empty, no smaller element exists on the left
            if not stack:
                result.append(-1)
            else:
                # Top of the stack is the nearest smaller element to the left
                result.append(stack[-1])
                
            # Push the current element onto the stack
            stack.append(num)
            
        return result
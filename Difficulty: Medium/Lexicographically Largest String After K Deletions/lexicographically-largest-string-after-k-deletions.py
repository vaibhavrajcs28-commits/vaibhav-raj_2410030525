class Solution:
    def maxSubseq(self, s, k):
        stack = []
        
        for char in s:
            # While the stack is not empty, the current character is larger than the top,
            # and we still have allowed deletions left
            while stack and stack[-1] < char and k > 0:
                stack.pop()
                k -= 1 # Consume one deletion
            
            stack.append(char)
            
        # If we still have deletions left over after the loop,
        # remove characters from the end of our monotonic sequence
        if k > 0:
            stack = stack[:-k]
            
        # Join the remaining characters back into a string
        return "".join(stack)
class Solution:
    def minParentheses(self, s):
        open_needed = 0   # Count of '(' we need to add
        close_needed = 0  # Count of ')' we need to add
        
        for char in s:
            if char == '(':
                # This open bracket will need a matching closing bracket
                close_needed += 1
            else: # char == ')'
                if close_needed > 0:
                    # It successfully matches with an existing open bracket
                    close_needed -= 1
                else:
                    # No open bracket is available to match, we must insert an opening bracket
                    open_needed += 1
                    
        # Total additions required to make the entire string valid
        return open_needed + close_needed
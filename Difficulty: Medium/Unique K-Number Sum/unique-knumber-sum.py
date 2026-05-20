class Solution:
    # Removed the ': int', '-> List[List[int]]' type annotations
    def combinationSum(self, n, k):
        ans = []
        
        def backtrack(start_num, current_combination, target_sum):
            # Base Case 1: If we have picked exactly k numbers
            if len(current_combination) == k:
                # If they sum up to n, save a copy of this combination
                if target_sum == 0:
                    ans.append(list(current_combination))
                return
            
            # Pruning Optimization: Stop if the target sum goes negative
            if target_sum < 0:
                return
                
            # Iterate through the valid number range [1, 9]
            for num in range(start_num, 10):
                # Include the number
                current_combination.append(num)
                
                # Move to the next number (num + 1) to ensure uniqueness
                backtrack(num + 1, current_combination, target_sum - num)
                
                # Backtrack: Remove the number
                current_combination.pop()
                
        # Start backtracking from number 1 with an empty combination tracker
        backtrack(1, [], n)
        return ans
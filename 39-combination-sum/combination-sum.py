class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(i, current_combination, current_target):
            # Base Case 1: Successfully formed a valid combination
            if current_target == 0:
                ans.append(list(current_combination))
                return
            
            # Base Case 2: Exceeded target value or out of bounds
            if current_target < 0 or i >= len(candidates):
                return
                
            # Choice 1: Include candidates[i] in the combination
            # We don't increment 'i' because the same element can be chosen multiple times
            current_combination.append(candidates[i])
            backtrack(i, current_combination, current_target - candidates[i])
            
            # Backtrack step: remove the last added element before exploring Choice 2
            current_combination.pop()
            
            # Choice 2: Skip candidates[i] and move to the next candidate element
            backtrack(i + 1, current_combination, current_target)
            
        # Start backtracking from index 0 with an empty combination tracker
        backtrack(0, [], target)
        return ans
        
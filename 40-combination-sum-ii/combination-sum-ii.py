class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # Step 1: Sort candidates to handle duplicates easily
        candidates.sort()
        
        def backtrack(start_idx, current_combination, current_target):
            # Base Case 1: Target reached
            if current_target == 0:
                ans.append(list(current_combination))
                return
            
            # Base Case 2: Target exceeded
            if current_target < 0:
                return
            
            # Explore choices for the current position in the combination
            for i in range(start_idx, len(candidates)):
                # If the current element is greater than the remaining target, 
                # all subsequent elements will also be too large because the array is sorted.
                if candidates[i] > current_target:
                    break
                
                # Skip duplicate elements at the same recursion depth level
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the element
                current_combination.append(candidates[i])
                
                # Move to the next element (i + 1) since each number can be used only once
                backtrack(i + 1, current_combination, current_target - candidates[i])
                
                # Backtrack
                current_combination.pop()
                
        # Start backtracking from index 0
        backtrack(0, [], target)
        return ans
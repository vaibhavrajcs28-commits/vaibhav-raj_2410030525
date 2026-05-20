class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(i, current_subset):
            # Base Case: If we've made a choice for every element in the array
            if i == len(nums):
                # Append a copy of the current subset to our answers list
                ans.append(list(current_subset))
                return
            
            # Choice 1: Include nums[i] in the subset
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            
            # Backtrack: Remove nums[i] to explore the alternate choice
            current_subset.pop()
            
            # Choice 2: Exclude nums[i] from the subset
            backtrack(i + 1, current_subset)
            
        # Start backtracking from index 0 with an empty subset
        backtrack(0, [])
        return ans
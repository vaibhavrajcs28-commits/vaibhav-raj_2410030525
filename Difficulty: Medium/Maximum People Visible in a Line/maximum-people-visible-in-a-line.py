class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # nge[i] stores the index of the next element >= arr[i]. 
        # If none exists, the view goes all the way to index n.
        nge = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[i] >= arr[stack[-1]]:
                popped_idx = stack.pop()
                nge[popped_idx] = i
            stack.append(i)
            
        # pge[i] stores the index of the previous element >= arr[i].
        # If none exists, the view goes all the way back to index -1.
        pge = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                popped_idx = stack.pop()
                pge[popped_idx] = i
            stack.append(i)
            
        # Calculate the maximum people seen by any single person
        max_visible = 0
        for i in range(n):
            # Formula: (nge[i] - 1) - (pge[i] + 1) + 1 simplifies to nge[i] - pge[i] - 1
            visible_count = nge[i] - pge[i] - 1
            max_visible = max(max_visible, visible_count)
            
        return max_visible
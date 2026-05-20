class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        # Initialize an array to store the index of the Next Smaller Element (NSE)
        # Default value is 'n' because if there is no smaller element, 
        # the subarray can extend to the very end of the array.
        nse = [n] * n
        stack = []
        
        # Traverse the array from left to right to find the NSE for each element
        for i in range(n):
            # While stack is not empty and the current element is strictly smaller 
            # than the element represented by the index at the top of the stack
            while stack and arr[i] < arr[stack[-1]]:
                popped_index = stack.pop()
                nse[popped_index] = i
            
            # Push the current index onto the stack
            stack.append(i)
            
        # Total valid subarrays count
        total_subarrays = 0
        for i in range(n):
            # For each starting index i, it can form (nse[i] - i) valid subarrays
            total_subarrays += (nse[i] - i)
            
        return total_subarrays
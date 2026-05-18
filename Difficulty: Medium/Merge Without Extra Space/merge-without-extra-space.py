class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        # Initialize pointers
        left = n - 1   # Points to the largest element of array 'a'
        right = 0      # Points to the smallest element of array 'b'
        
        # Swap elements if they are out of order across arrays
        while left >= 0 and right < m:
            if a[left] > b[right]:
                # Swap the elements
                a[left], b[right] = b[right], a[left]
                left -= 1
                right += 1
            else:
                # Since the arrays are sorted, if a[left] <= b[right], 
                # all elements before 'left' are also smaller than 'b[right]'
                break
                
        # Re-sort both arrays individually to restore correct internal order
        a.sort()
        b.sort()
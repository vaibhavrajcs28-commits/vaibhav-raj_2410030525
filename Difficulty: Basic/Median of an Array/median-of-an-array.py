class Solution:
    def findMedian(self, arr):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)
        
        # Step 2: Check if the number of elements is odd or even
        if n % 2 != 0:
            # Odd number of elements: return the middle element
            return arr[n // 2]
        else:
            # Even number of elements: return average of the two middle elements
            mid1 = arr[(n // 2) - 1]
            mid2 = arr[n // 2]
            # Use floating point division to get correct decimal results (e.g., 61.5)
            # Use floor division or int cast if the platform strictly expects an integer floor value for pure ints, 
            # but given the examples show "61.5", a float/value division is correct.
            return (mid1 + mid2) / 2
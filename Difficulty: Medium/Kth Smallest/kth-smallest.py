class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        return arr[k-1]

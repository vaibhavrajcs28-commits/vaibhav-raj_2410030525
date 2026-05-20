class Solution:
    def sortByLength(self, arr):
        # Python's built-in sort() uses Timsort, which is a stable sorting algorithm.
        # Setting key=len will sort the strings by their length while automatically
        # maintaining the original relative order of strings with identical lengths.
        arr.sort(key=len)
        return arr
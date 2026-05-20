import heapq

class Solution:
    # 'List[int]' हटाकर सिर्फ 'arr' रहने दें
    def minOperations(self, arr):
        initial_sum = sum(arr)
        target_reduction = initial_sum / 2
        
        max_heap = [-float(num) for num in arr]
        heapq.heapify(max_heap)
        
        current_reduction = 0.0
        operations = 0
        
        while current_reduction < target_reduction:
            largest = -heapq.heappop(max_heap)
            half_value = largest / 2.0
            current_reduction += half_value
            operations += 1
            heapq.heappush(max_heap, -half_value)
            
        return operations
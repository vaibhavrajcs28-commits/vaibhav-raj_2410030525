from collections import defaultdict

class Solution:
    def countPairs(self, arr):
        # Hash map to track the frequency of each wildcard pattern
        pattern_counts = defaultdict(int)
        total_pairs = 0
        
        # Traverse through each string in the input array
        for string in arr:
            # Generate all possible wildcard patterns by masking one character at a time
            for i in range(len(string)):
                # Create the pattern: substring before index 'i' + '*' + substring after index 'i'
                pattern = string[:i] + '*' + string[i+1:]
                
                # If this pattern was seen before, it means the current string forms a 
                # valid 1-mismatch pair with all previously logged strings sharing this pattern.
                total_pairs += pattern_counts[pattern]
                
                # Update the pattern frequency in our tracker
                pattern_counts[pattern] += 1
                
        return total_pairs
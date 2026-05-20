from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hash map where values are lists by default
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string alphabetically to find its baseline signature
            # e.g., 'tea' -> ['a', 'e', 't'] -> 'aet'
            sorted_s = "".join(sorted(s))
            
            # Group the original string under its sorted signature key
            anagram_map[sorted_s].append(s)
            
        # Return all grouped lists from the hash map
        return list(anagram_map.values())
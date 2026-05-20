from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the occurrences of each character
        freq_map = Counter(s)
        
        # Step 2: Get unique characters and sort them
        # Primary key: freq_map[char] (ascending frequency)
        # Secondary key: char (lexicographical order)
        sorted_chars = sorted(freq_map.keys(), key=lambda char: (freq_map[char], char))
        
        # Step 3: Rebuild the string by multiplying character string representations
        result = []
        for char in sorted_chars:
            result.append(char * freq_map[char])
            
        return "".join(result)
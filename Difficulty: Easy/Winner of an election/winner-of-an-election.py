from collections import Counter

class Solution:
    def winner(self, arr):
        # Step 1: Count the total votes for each candidate
        vote_counts = Counter(arr)
        
        # Initialize tracking variables for the winner
        winner_name = ""
        max_votes = -1
        
        # Step 2: Traverse through the unique candidates
        for candidate, votes in vote_counts.items():
            # Condition A: Current candidate has strictly more votes
            if votes > max_votes:
                max_votes = votes
                winner_name = candidate
            # Condition B: It's a tie, break it lexicographically (alphabetically)
            elif votes == max_votes:
                if candidate < winner_name:
                    winner_name = candidate
                    
        # Step 3: Return an array containing the name and the stringified vote count
        return [winner_name, str(max_votes)]
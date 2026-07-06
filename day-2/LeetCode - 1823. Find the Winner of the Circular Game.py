# Time complexity: O(n)
# Space complexity: O(n)  
# Method: recursion stack
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper_function(n):
            # Base case:
            # If there is only one player, they are the winner.
            # Return 0 because we are using 0-based indexing.
            if n == 1:
                return 0

            # Find the winner for (n - 1) players, then adjust the winner's position after adding the nth player.
            return (helper_function(n - 1) + k) % n

        # Convert the 0-based answer to 1-based indexing.
        return helper_function(n) + 1


# Time complexity: O(n)
# Space complexity: O(1)
# Method: iterative
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Start with one player.
        # The winner's index is 0 (0-based indexing).
        winner = 0

        # Build the answer from 2 players up to n players.
        for i in range(2, n + 1):
            # Update the winner's position after adding one more player to the circle.
            winner = (winner + k) % i

        # Convert the 0-based answer to 1-based indexing.
        return winner + 1

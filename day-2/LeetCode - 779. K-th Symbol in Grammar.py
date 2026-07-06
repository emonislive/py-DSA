# Time complexity: O(n)
# Space complexity: O(n)
# Method 1: Which half am I in?
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case:
        # The first row has only one value: 0
        if n == 1:
            return 0

        # Find the middle of the current row
        rowLen = 2 ** (n - 1)
        mid = rowLen // 2

        # The first half of the current row is the same as the previous row
        # The second half is the previous row, but every value is flipped

        if k <= mid:
            # If k is in the first half, its value is the same as the value at the same k-th position in the previous row
            return self.kthGrammar(n - 1, k)
        else:
            # If k is in the second half, subtract mid to get the matching position in the first half
            # We need to flip the value at that position in the previous row to get the answer
            return int(not self.kthGrammar(n - 1, k - mid))



# Time complexity: O(n)
# Space complexity: O(n)
# Method 2: Who is my parent?
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case:
        # The first row has only one value: 0
        if n == 1:
            return 0

        # Find the parent of the current position
        # Every two positions in the current row come from one position in the previous row
        parent = self.kthGrammar(n - 1, (k // 2) + (k % 2))

        # Even positions are the second child of the parent, and the second child is always the opposite value
        flip = False
        if k % 2 == 0:
            flip = True

        if flip:
            # Flip the parent's value
            return int(not parent)
        else:
            # Odd positions are the first child, so they have the same value as the parent
            return parent
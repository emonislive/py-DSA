# Time complexity: O(n * 2^n)
# Space complexity: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []

        def backtrack(nums, index, output):
            # Base condition:
            # Reached a leaf node of the recursion tree, so store the current subset.
            if index == n:
                subset.append(output[:])
                return

            backtrack(nums, index + 1, output)  # Traverse the left branch of the recursion tree without adding the current element.
            output.append(nums[index])          # Add the current element to the current subset.
            backtrack(nums, index + 1, output)  # Traverse the right branch of the recursion tree with the current element included.
            output.pop()                        # Remove the last added element to restore the previous state while backtracking.
            
        backtrack(nums, 0, [])
        return subset


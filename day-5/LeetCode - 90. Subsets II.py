# Time complexity: O(n * 2^n)
# Space complexity: O(n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []

        # Sort the array so that duplicate elements are adjacent.
        # This allows us to skip consecutive duplicates easily.
        nums.sort()

        def backtrack(index, output):
            # Base condition:
            # Reached a leaf node of the recursion tree, so store the current subset.
            if index == n:
                subset.append(output.copy())  # Same as output[:]
                return

            # Include the current element and traverse deeper into the recursion tree.
            output.append(nums[index])
            backtrack(index + 1, output)            
            output.pop()                                                 # Remove the last added element to restore the previous state while backtracking.
            
            # Exclude the current element, skip all consecutive duplicates to prevent generating the same subset multiple times.
            while index < n - 1 and nums[index] == nums[index + 1]:      
                index += 1

            backtrack(index + 1, output)                                 # Continue traversing the recursion tree after skipping the duplicate elements.

        backtrack(0, [])
        return subset 
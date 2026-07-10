# Time Complexity: O(N^(T/M))ss
# N = number of candidates, T = target, M = smallest candidate
# The recursion tree has a maximum depth of T/M, and each level explores up to N choices.

# Space Complexity: O(T/M)
# For the recursion stack and the current combination. Excluding the space required for the output list.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(index, curr, tot_sum):
            # Base case
            if tot_sum == target:
                answer.append(curr.copy())
                return
            
            # Pruning
            if tot_sum > target:
                return
            
            for i in range(index, len(candidates)):
                # Choose
                curr.append(candidates[i])
                
                # Explore
                tot_sum += candidates[i]
                backtrack(i, curr, tot_sum)
                tot_sum -= candidates[i]

                # Backtrack
                curr.pop()

        backtrack(0, [], 0)
        return answer

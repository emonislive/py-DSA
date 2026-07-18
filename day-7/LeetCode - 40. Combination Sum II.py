# Time complexity: O(n * 2^n)
# n = number of candidates.
# In the worst case, the algorithm explores all possible subsets (2^n).
# Copying each valid combination takes O(N), resulting in O(n * 2^n).
# Sorting the candidates initially takes O(n log n).

# Space complexity: O(n)
# For the recursion stack and the current combination.
# Excluding the space required for the output list.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def backtrack(index, curr, tot_sum):
            # Base case
            if tot_sum == target:
                answer.append(curr.copy())
                return
            
            # Pruning
            if tot_sum > target:
                return
            
            hash = {}
            for i in range(index, len(candidates)):
                # Check for duplicates
                if candidates[i] not in hash:
                    hash[candidates[i]] = True
                    
                    # Choose
                    curr.append(candidates[i])

                    # Explore
                    tot_sum += candidates[i]
                    backtrack(i + 1, curr, tot_sum)
                    tot_sum -= candidates[i]

                    # Backtrack
                    curr.pop()

        backtrack(0, [], 0)
        return answer
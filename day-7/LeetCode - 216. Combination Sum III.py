# Time complexity: O(C(9, k) * k)
# k = required number of elements in each combination.
# The algorithm explores all possible combinations of choosing k numbers from 1 to 9.
# There are C(9, k) such combinations, and copying each valid combination
# into the answer list takes O(k) time.

# Space complexity: O(k)
# For the recursion stack and the current combination.
# Excluding the space required for the output list.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []

        def backtrack(index, curr, tot_sum):
            # Base case
            if len(curr) == k and tot_sum == n:
                answer.append(curr.copy())
                return
            
            # Pruning 
            if len(curr) > k or tot_sum > n:
                return
            
            hash = {}
            for i in range(index, 10):
                # Check for duplicates
                if i not in hash:
                    hash[i] = True

                    # Choose
                    curr.append(i)

                    # Explore
                    tot_sum += i
                    backtrack(i + 1, curr, tot_sum)
                    tot_sum -= i

                    # Backtrack
                    curr.pop()


        backtrack(1, [], 0)
        return answer
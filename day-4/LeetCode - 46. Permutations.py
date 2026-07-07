# Time complexity: O(n * n!)
# Space complexity: O(n)
# Method 1: Backtracking with Temporary Path
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp, answer = [], []
        n = len(nums)

        def backtrack(index):
            if index == n:
                answer.append(temp[:]) 
                return

            for i in nums: 
                if i not in temp:
                    temp.append(i)
                    backtrack(index + 1)
                    temp.pop()
        index = 0       
        backtrack(index)
        return answer



# Time complexity: O(n * n!)
# Space complexity: O(n)
# Method 2: Swap-based Backtracking (In-place)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(index):
            if index == n - 1:
                res.append(nums[:])
                return

            for i in range(index, n):
                    nums[i], nums[index] = nums[index], nums[i]
                    backtrack(index + 1)
                    nums[index], nums[i] = nums[i], nums[index]

        backtrack(0)
        return res
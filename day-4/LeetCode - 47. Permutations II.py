# Time complexity: O(n x n!)
# Space complexity: O(n)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(index):
            if index == n - 1:
                res.append(nums[:])
                return
            hash = {}
            for i in range(index, n):
                if nums[i] not in hash:
                    hash[nums[i]] = True
                    nums[i], nums[index] = nums[index], nums[i]
                    backtrack(index + 1)
                    nums[index], nums[i] = nums[i], nums[index]

        backtrack(0)
        return res
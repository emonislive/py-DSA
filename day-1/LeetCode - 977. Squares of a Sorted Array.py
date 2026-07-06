# Method 1
# Time complexity: O(n log n)
# Space complexity: O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums


# Method 2
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        newArr = [0] * size
        left, right = 0, size - 1
        for i in reversed(range(size)):
            if nums[left] ** 2 > nums[right] ** 2:
                newArr[i] = nums[left] ** 2
                left += 1
            else:
                newArr[i] = nums[right] ** 2
                right -= 1
        return newArr
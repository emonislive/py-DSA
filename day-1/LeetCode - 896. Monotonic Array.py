class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasingFlag = True
        decreasingFlag = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasingFlag = False
            elif nums[i] < nums[i + 1]:
                decreasingFlag = False
                
        if increasingFlag or decreasingFlag:
            return True
        else:
            return False

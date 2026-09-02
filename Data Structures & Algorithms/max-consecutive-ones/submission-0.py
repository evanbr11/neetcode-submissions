class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            count = 0
            j = i
            while j < len(nums) and nums[j] == 1:
                count += 1
                j += 1
            res = max(res, count)
            i = j
        return res

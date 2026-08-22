class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, l = 0, 0

        while l < len(nums):
            if nums[l] != val:
                nums[k] = nums[l]
                k += 1
            l += 1
        return k
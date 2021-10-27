# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0

        while i < len(nums) and j < len(nums):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        j = i
        while i < len(nums) and j < len(nums):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

    def sortColorsV2(self, nums: List[int]) -> None:

        low = mid = 0
        high = len(nums) - 1

        while 
        pass

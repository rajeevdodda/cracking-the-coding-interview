# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max, global_max = nums[0], nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)
        return global_max


solution = Solution()

print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

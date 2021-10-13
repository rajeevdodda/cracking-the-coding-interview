# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        j = 0
        for i in nums:
            if target - i in hash_map:
                return [hash_map[target - i], j]
            else:
                hash_map[i] = j
            j += 1

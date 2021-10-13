# https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()

        for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map.add(i)
        else:
            return False


solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

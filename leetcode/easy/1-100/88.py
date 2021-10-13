# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        while i < m:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                k = j
                while k < n - 1:
                    if nums2[k] > nums2[k + 1] :
                        nums2[k], nums2[k + 1] = nums2[k + 1], nums2[k]
                        k += 1
                    else:
                         break
        while j < n:
            nums1[i + j] = nums2[j]
            j += 1


solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)

print(nums1)



# https://leetcode.com/problems/guess-number-higher-or-lower/


def guess():
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = 2 ** 31 - 1
        while True:
            mid = (low + high) // 2
            ans = guess(mid)
            if ans == -1:
                high = mid - 1
            elif ans == 1:
                low = mid + 1
            else:
                return mid

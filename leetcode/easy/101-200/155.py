# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.data = []
        self.min_value = float("inf")

    def push(self, val: int) -> None:
        self.min_value = min(self.min_value, val)
        self.data.append((val, self.min_value))

    def pop(self) -> None:
        x, y = self.data.pop()
        if self.data:
            if x == self.min_value:
                self.min_value = self.data[-1][1]
        else:
            self.min_value = float("inf")

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.min_value

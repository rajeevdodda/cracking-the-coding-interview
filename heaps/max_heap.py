class MaxHeap:
    def __init__(self) -> None:
        self.size = 0
        self.data = [0]

    def sift_up(self, index):
        while index // 2 > 0:
            if self.data[index] < self.data[index // 2]:
                self.data[index], self.data[index // 2] = (
                    self.data[index // 2],
                    self.data[index],
                )
            index = index  // 2

    def insert(self, key):
        self.data.append(key)
        self.size += 1
        self.sift_up(self.size)

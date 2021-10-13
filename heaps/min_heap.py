import heapq


class MinHeap:
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
            index = index // 2

    def insert(self, key):
        self.data.append(key)
        self.size += 1
        self.sift_up(self.size)

    def sift_down(self, index):
        i = index
        j = 2 * i

        while j < self.size:
            if self.data[j + 1] < self.data[j]:
                j += 1

            if self.data[i] > self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i = j
                j = 2 * j
            else:
                break
        
    def delete(self):
        if len(self.data) == 1:
            return "Empty heap"
        min_key = self.data[1]
        self.data[1] = self.data[self.size]
        self.data.pop()
        self.size -= 1
        self.sift_down(1)
        return min_key


heap = MinHeap()

heap.insert(5)
heap.insert(9)
heap.insert(11)
heap.insert(14)
heap.insert(18)
heap.insert(19)
heap.insert(21)
heap.insert(33)
heap.insert(17)
heap.insert(27)

print(heap.data)

heap.insert(7)
print(heap.data)


print(heap.delete())
print(heap.data)
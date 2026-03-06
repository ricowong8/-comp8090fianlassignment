class Heap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        """Import new element to heap"""
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def extract_max(self):
        """Extract maximum value (max heap)"""
        if len(self.data) == 0:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.data[index] > self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.data) and self.data[left] > self.data[largest]:
            largest = left
        if right < len(self.data) and self.data[right] > self.data[largest]:
            largest = right

        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self._heapify_down(largest)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(4)
    heap.insert(15)
    heap.insert(20)

    print("Heap data:", heap.data)
    print("Extract max:", heap.extract_max())
    print("Heap after extract:", heap.data)

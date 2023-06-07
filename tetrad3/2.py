import heapq


class BinaryHeap:
    def __init__(self, arr=[]):
        self.heap = arr
        heapq.heapify(self.heap)

    def insert(self, x):
        heapq.heappush(self.heap, x)

    def remove_maximum(self):
        if len(self.heap) == 0:
            raise RuntimeError("Heap is empty")
        return heapq.heappop(self.heap)

    def get_maximum(self):
        if len(self.heap) == 0:
            raise RuntimeError("Heap is empty")
        return self.heap[0]


if __name__ == '__main__':
    # Create an empty binary heap
    heap1 = BinaryHeap()

    # Create a binary heap from a list of integers
    arr = [3, 7, 1, 9, 2]
    heap2 = BinaryHeap(arr)

    # Insert a new element into the heap
    heap1.insert(5)

    # Remove the maximum element from the heap
    max_val = heap2.remove_maximum()

    # Get the maximum element of the heap
    max_val2 = heap2.get_maximum()

    # Print the results
    print("Heap 1: ")
    print("Maximum: ", heap1.get_maximum())

    print()

    print("Heap 2: ")
    print("Original array: ", arr)
    print("Maximum removed: ", max_val)
    print("New maximum: ", max_val2)

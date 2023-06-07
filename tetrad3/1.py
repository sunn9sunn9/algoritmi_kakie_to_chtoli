def minHeapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # left child = 2*i + 1
    right = 2 * i + 2  # right child = 2*i + 2

    # If left child is smaller than root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If right child is smaller than smallest so far
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not root
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        # Recursively heapify the affected sub-tree
        minHeapify(arr, n, smallest)


def buildMinHeap(arr, n):
    # Index of last non-leaf node
    startIdx = (n // 2) - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        minHeapify(arr, n, i)


n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

# Build min heap
buildMinHeap(arr, n)

# Print the min heap
print("Min Heap:", end=" ")
for i in range(n):
    print(arr[i], end=" ")
print()
